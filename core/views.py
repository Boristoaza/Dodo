from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Empresas
from django.contrib.auth.models import User
from django.contrib import messages

def main_view(request):
     if not request.user.is_authenticated:
        return redirect('usuarios:login')
     return render(request, 'home.html')

@login_required
def home_view(request):
    return render(request,'home.html')

@login_required
def frontmant_view(request):
    return render(request,'frontmant.html')


@login_required
def registrar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        username = request.POST.get('username')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        contrasenia = request.POST.get('contrasenia')

        nombre_empresa = request.POST.get('nombre_empresa')
        ruc = request.POST.get('ruc')
        correo_empresa = request.POST.get('correo_empresa')
        telefono_empresa = request.POST.get('telefono_empresa')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')
        actividad = request.POST.get('actividad')

        nombre_usuario = User.objects.filter(username=username).exists()

        if not nombre_usuario:
            crear_cliente = User.objects.create_user(
                username=username,
                first_name=nombre,
                last_name=apellido,
                email=correo,
                password=contrasenia
            )

            crear_empresa = Empresas.objects.create(
                usuario=crear_cliente,
                nombre_empresa=nombre_empresa,
                ruc=ruc,
                correo_empresa=correo_empresa,
                telefono_empresa=telefono_empresa,
                ciudad=ciudad,
                direccion=direccion,
                actividad=actividad
            )

    return render(request, 'registro_cliente.html')