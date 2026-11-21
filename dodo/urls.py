from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls',namespace='core')),
    path('', include('usuarios.urls',namespace='usuarios')),
    path('',include('productos.urls',namespace='productos')),
    path('',include('inventario.urls',namespace='inventario')),
    path('',include('ventas.urls',namespace='ventas')),
    path('',include('proveedores.urls',namespace='proveedores')),
    path('',include('compras.urls',namespace='compras')),
    path('',include('administracion.urls',namespace='administracion')),
    path('',include('empresas.urls',namespace='empresas')),
    path('', include('facturacion.urls', namespace='facturacion')),


    path("__reload__/", include("django_browser_reload.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
