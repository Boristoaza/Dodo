from django.urls import path
from . import views

app_name = "facturacion"

urlpatterns = [
    path('facturacion/', views.facturacion_view, name="facturacion")
]