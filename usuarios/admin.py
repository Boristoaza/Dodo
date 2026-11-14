from django.contrib import admin
from .models import Roles , Cargos_laborales,Usuario_cargo_permiso
# Register your models here.
admin.site.register(Roles)
admin.site.register(Cargos_laborales)
admin.site.register(Usuario_cargo_permiso)