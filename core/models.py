from django.db import models
from django.utils.translation import gettext_lazy as _


class Modulos(models.Model):

    class Modulos_app(models.TextChoices):
        PRODUCTO = "PDT", _("Producto")
        INVENTARIO = "INV", _("Inventario")
        PROVEEDORES = "PVR", _("Proveedores")
        COMPRAS = "CMP", _("Compras")
        FACTURACION = "FTN", _("Facturación")
        EMPRESA = "EMP", _("Empresa")
        ADMINISTRACION = "AMD", _("Administración")
        VENTAS = "VNT", _("Ventas")

    nombre = models.CharField(
        max_length=3,
        choices=Modulos_app.choices,
        unique=True
    )