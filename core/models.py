
from django.db import models
from django.contrib.auth.models import User


class Empresas(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='empresa'
    )

    nombre_empresa = models.CharField(max_length=150)
    ruc = models.CharField(max_length=13, unique=True)
    correo_empresa = models.EmailField(unique=True)
    telefono_empresa = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    actividad = models.CharField(max_length=150)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre_empresa
