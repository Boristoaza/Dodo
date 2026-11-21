
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cargo_laborales(models.Model):

    class Cargos(models.TextChoices):
        GERENTE = "GRT", _("Gerente")
        ADMINISTRADOR = "ADM", _("Administrador")
        SUPERVISOR = "SPV", _("Supervisor")
        FARMACEUTICO = "FAR", _("Farmacéutico")
        AUXILIAR_FARMACIA = "AXF", _("Auxiliar de farmacia")
        CAJERO = "CJR", _("Cajero")
        VENDEDOR = "VND", _("Vendedor")
        BODEGUERO = "BDG", _("Bodeguero")
        CONTADOR = "CNT", _("Contador")
        INVENTARIO = "INV", _("Encargado de inventario")
        RECEPCIONISTA = "REC", _("Recepcionista")
        REPARTIDOR = "RPD", _("Repartidor")
        LIMPIEZA = "LMP", _("Personal de limpieza")

    cargo_laboral = models.CharField(
        max_length=3,
        choices=Cargos.choices,
        default=Cargos.CAJERO
    )
    class Meta:
        verbose_name = 'Cargo_laboral'
        verbose_name_plural = 'Cargo_laboreles'

    def __str__(self):
        return self.get_cargo_laboral_display()


class Modulos(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'

    def __str__(self):
        return self.nombre


class Permisos(models.Model):

    class Acciones(models.TextChoices):
        CONSULTAR = "view", _("Consultar")
        CREAR = "add", _("Crear")
        EDITAR = "change", _("Editar")
        ELIMINAR = "delete", _("Eliminar")
        APROBAR = "approve", _("Aprobar")
        ANULAR = "cancel", _("Anular")
        EXPORTAR = "export", _("Exportar")

    modulo = models.ForeignKey(
        Modulos,
        on_delete=models.PROTECT,
        related_name="permisos"
    )

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, unique=True)
    accion = models.CharField(
        max_length=10,
        choices=Acciones.choices
    )

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'

        constraints = [
            models.UniqueConstraint(
                fields=["modulo", "accion"],
                name="unique_permiso_modulo_accion"
            )
        ]

    def __str__(self):
        return f"{self.modulo.nombre} - {self.nombre}"


class Roles(models.TextChoices):
    SUPERUSUARIO = 'SUP', 'Superusuario'
    ADMIN_EMPRESA = 'ADM', 'Administrador de empresa'
    EMPLEADO = 'EMP', 'Empleado'

    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = 'Roles'