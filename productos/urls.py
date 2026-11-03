from django.urls import path

from . import views

app_name="productos"

urlpatterns = [
    path('productos/',views.productos,name='productos'),
    path('registrar_productos/',views.registrar_productos, name='registrar_productos'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
]