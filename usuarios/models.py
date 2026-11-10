from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Roles(models.Model):

    class Roles_dodo(models.IntegerChoices):
        SUPERUSUARIO = 2, "Superusuario"
        EJECUTIVO = 1, "Ejecutivo"
        EMPLEADO = 0, "Empleado"

    roles_in_dodo = models.IntegerField(
        choices=Roles_dodo.choices,
        default=Roles_dodo.SUPERUSUARIO
    )

    class Meta:
        verbose_name_plural = 'Roles'

    def is_upperclass(self):
        return self.roles_in_dodo in {
            self.Roles_dodo.SUPERUSUARIO,
            self.Roles_dodo.EJECUTIVO,
        }


def rol_empleado():
    return Roles.objects.get(
        roles_in_dodo=Roles.Roles_dodo.EMPLEADO
    ).pk


class Usuarios_roles(models.Model):
   usuario = models.ForeignKey(User,on_delete=models.CASCADE)
   roles = models.ForeignKey(Roles,on_delete=models.CASCADE , default=rol_empleado)


class Cargos_laborales(models.Model):

    class Cargos(models.TextChoices):
        GERENTE = "GER", _("Gerente")
        ADMINISTRADOR = "ADM", _("Administrador")
        SUPERVISOR = "SUP", _("Supervisor")
        JEFE_SUCURSAL = "JFS", _("Jefe de sucursal")
        FARMACEUTICO = "FAR", _("Farmacéutico")
        AUXILIAR_FARMACIA = "AUX", _("Auxiliar de farmacia")
        DEPENDIENTE = "DEP", _("Dependiente de farmacia")
        CAJERO = "CAJ", _("Cajero")
        VENDEDOR = "VEN", _("Vendedor")
        BODEGUERO = "BOD", _("Bodeguero")
        CONTADOR = "CON", _("Contador")
        ASISTENTE_ADMINISTRATIVO = "ASA", _("Asistente administrativo")

    cargo = models.CharField(
        max_length=3,
        choices=Cargos.choices,
        default=Cargos.VENDEDOR,
    )

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos_laborales'

    def __str__(self):
        return self.get_cargo_display()