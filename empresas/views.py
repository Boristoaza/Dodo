from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Empresas,Sucursales
from django.contrib.auth.models import User


# Create your views here.
def empresas_view(request):
    return render(request,'empresa.html')

@login_required
def registrar_empresa_view(request):
    if request.method == 'POST':

        # DATOS DEL REPRESENTANTE LEGAL
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        username = request.POST.get('username')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        contrasenia = request.POST.get('contrasenia')

        # DATOS DE LA EMPRESA
        nombre_empresa = request.POST.get('nombre_empresa')
        ruc = request.POST.get('ruc')
        correo_empresa = request.POST.get('correo_empresa')
        telefono_empresa = request.POST.get('telefono_empresa')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')
        actividad = request.POST.get('actividad')

        # CREAR USUARIO
        crear_usuario = User.objects.create_user(
            username=username,
            first_name=nombre,
            last_name=apellido,
            email=correo,
            password=contrasenia
        )

        # CREAR EMPRESA
        crear_empresa = Empresas.objects.create(
            usuario=crear_usuario,
            nombre_empresa=nombre_empresa,
            ruc=ruc,
            correo_empresa=correo_empresa,
            telefono_empresa=telefono_empresa,
            ciudad=ciudad,
            direccion=direccion,
            actividad=actividad
        )

    return render(request, 'forms/registrar_empresa.html')