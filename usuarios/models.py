
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


# class Permisos(models.Model):

#     class Acciones(models.TextChoices):
#         CONSULTAR = "view", _("Consultar")
#         CREAR = "add", _("Crear")
#         EDITAR = "change", _("Editar")
#         ELIMINAR = "delete", _("Eliminar")
#         APROBAR = "approve", _("Aprobar")
#         ANULAR = "cancel", _("Anular")
#         EXPORTAR = "export", _("Exportar")

#     modulo = models.ForeignKey(
#         Modulos,
#         on_delete=models.PROTECT,
#         related_name="permisos"
#     )

#     nombre = models.CharField(max_length=100)
#     codigo = models.CharField(max_length=100, unique=True)
#     accion = models.CharField(
#         max_length=10,
#         choices=Acciones.choices
#     )

#     class Meta:
#         verbose_name = 'Permiso'
#         verbose_name_plural = 'Permisos'

#         constraints = [
#             models.UniqueConstraint(
#                 fields=["modulo", "accion"],
#                 name="unique_permiso_modulo_accion"
#             )
#         ]

#     def __str__(self):
#         return f"{self.modulo.nombre} - {self.nombre}"


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
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
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


class AsignacionUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursales, on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Asignación de usuario'
        verbose_name_plural = 'Asignaciones de usuarios'

    def __str__(self):
        return f'{self.usuario} - {self.empresa} - {self.sucursal}'




