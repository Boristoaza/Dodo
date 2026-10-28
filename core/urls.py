from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('home/', views.home_view, name='home'),
    path('frontmant/', views.frontmant_view, name='frontmant'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
]
