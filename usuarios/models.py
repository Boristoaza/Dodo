from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Roles(models.Model):
    class Roles_dodo(models.TextChoices):
     SUPERUSER = "SPU", _("superusuario")
     ADMIN_EMPRESA = "ADE", _("Administrador de empresa")
     SUPERVISOR = "SPV" ,_("supervisro")
     VENDEDOR = "VND",_("vendedor")
    roles_in_dodo = models.CharField(
        max_length=3,
        choices=Roles_dodo,
        default=Roles_dodo.SUPERVISOR
    )

    class Meta:
        verbose_name_plural = 'Roles'

    def is_upperclass(self):
        return self.roles_in_dodo in {
            self.Roles_dodo.SUPERUSER,
            self.Roles_dodo.SUPERVISOR,
        }


class Usuarios_roles(models.Model):
   usuario = models.ForeignKey(User,on_delete=models.CASCADE)
   roles = models.ForeignKey(Roles,on_delete=models.CASCADE)
