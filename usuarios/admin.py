from django.contrib import admin
from usuarios.models import Cargo_laborales,Modulos , Roles , AsignacionUsuario , Modulos_permisos





admin.site.register(Cargo_laborales)
admin.site.register(Modulos)
admin.site.register(Roles)
admin.site.register(AsignacionUsuario)
admin.site.register(Modulos_permisos)

