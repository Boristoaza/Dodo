from django.contrib import admin
from .models import Empresas , Sucursales , Empleados

# Register your models here.

admin.site.register(Empresas)
admin.site.register(Sucursales)
admin.site.register(Empleados)