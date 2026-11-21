
from django.db import models
from django.contrib.auth.models import User
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

    def is_upperclass(self):
        return self.cargo_laboral in {
            self.Cargos.GERENTE,
            self.Cargos.ADMINISTRADOR,
            self.Cargos.SUPERVISOR,
        }

# class Permisos(models.Models):
#     class Permiso (models.TextChoices):
        