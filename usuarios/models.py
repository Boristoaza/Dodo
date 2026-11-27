
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from empresas.models import Empresas , Sucursales


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


class Roles(models.Model):

    class Tipos(models.TextChoices):
        SUPERUSUARIO = 'SUP', _('Superusuario')
        ADMIN_EMPRESA = 'ADM', _('Administrador de empresa')
        ADMIN_SUCURSAL = 'ASL' ,_('Administrador de sucursal')
        EMPLEADO = 'EMP', _('Empleado')

    nombre = models.CharField(
        max_length=100
    )

    codigo = models.CharField(
        max_length=3,
        choices=Tipos.choices,
        unique=True
    )

    descripcion = models.TextField(blank=True)

    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre

class Modulos_permisos(models.Model):
    empleado = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE , null=True , blank=True)

    consultar = models.BooleanField(default=False)
    crear = models.BooleanField(default=False)
    editar = models.BooleanField(default=False)
    eliminar = models.BooleanField(default=False)
    aprobar = models.BooleanField(default=False)
    anular = models.BooleanField(default=False)
    exportar = models.BooleanField(default=False)

    class Meta:
        unique_together = ('empleado', 'modulo')







