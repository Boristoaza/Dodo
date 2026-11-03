
from django.db import models
from django.core.validators import MinValueValidator


class Producto(models.Model):

    CATEGORIAS = [
        ('medicamento', 'Medicamento'),
        ('vitamina', 'Vitamina'),
        ('cuidado_personal', 'Cuidado personal'),
        ('otros', 'Otros'),
    ]

    FORMAS_FARMACEUTICAS = [
        ('tableta', 'Tableta'),
        ('capsula', 'Cápsula'),
        ('jarabe', 'Jarabe'),
        ('suspension', 'Suspensión'),
        ('crema', 'Crema'),
        ('inyectable', 'Inyectable'),
        ('otro', 'Otro'),
    ]

    VIAS_ADMINISTRACION = [
        ('oral', 'Oral'),
        ('topica', 'Tópica'),
        ('intramuscular', 'Intramuscular'),
        ('intravenosa', 'Intravenosa'),
        ('otra', 'Otra'),
    ]

    # Información general
    nombre_producto = models.CharField(max_length=200)
    codigo_barras = models.CharField(max_length=100, blank=True)
    laboratorio = models.CharField(max_length=150, blank=True)
    categoria = models.CharField(
        max_length=30,
        choices=CATEGORIAS
    )
    descripcion = models.TextField(blank=True)

    # Información farmacéutica
    principio_activo = models.CharField(max_length=200, blank=True)
    concentracion = models.CharField(max_length=100, blank=True)
    forma_farmaceutica = models.CharField(
        max_length=30,
        choices=FORMAS_FARMACEUTICAS,
        blank=True
    )
    via_administracion = models.CharField(
        max_length=30,
        choices=VIAS_ADMINISTRACION,
        blank=True
    )
    requiere_receta = models.BooleanField(default=False)

    # Presentaciones
    pastillas_por_blister = models.PositiveIntegerField(default=1)
    blisteres_por_caja = models.PositiveIntegerField(default=1)
    pastillas_por_caja = models.PositiveIntegerField(default=1)

    # Precios de venta
    precio_caja = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    precio_blister = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    precio_pastilla = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    # Imagen
    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )

    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto


class Lote(models.Model):

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='lotes'
    )

    # Identificación del lote
    numero_lote = models.CharField(max_length=100)
    fecha_fabricacion = models.DateField(
        blank=True,
        null=True
    )
    fecha_caducidad = models.DateField()

    # Costos de compra
    costo_caja = models.DecimalField(
        max_digits=10, decimal_places=4, default=0
    )
    costo_blister = models.DecimalField(
        max_digits=10, decimal_places=4, default=0
    )
    costo_pastilla = models.DecimalField(
        max_digits=10, decimal_places=4, default=0
    )

    # Inventario inicial
    stock_cajas = models.PositiveIntegerField(default=0)
    stock_blisteres = models.PositiveIntegerField(default=0)
    stock_pastillas = models.PositiveIntegerField(default=0)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['producto', 'numero_lote'],
                name='producto_numero_lote_unico'
            )
        ]
        ordering = ['fecha_caducidad']

    def __str__(self):
        return f'{self.producto.nombre_producto} - {self.numero_lote}'
