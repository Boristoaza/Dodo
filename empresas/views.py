
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Empresas, Sucursales, Empleados 
from usuarios.models import Roles



@login_required
def empresa_view(request):
    return render(request, 'views/empresa.html')


@login_required
def sucursal_view(request):
    sucursales = Sucursales.objects.all()

    contexto = {'sucursales':sucursales}
    return render(request, 'views/sucursal.html' , contexto)


@login_required
def crear_sucursal_view(request):

    if request.method == 'POST':

        nombre_sucursal = request.POST.get('nombre_sucursal')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')

        empresa = request.user.empresa

        Sucursales.objects.create(
            empresa=empresa,
            nombre_sucursal=nombre_sucursal,
            telefono=telefono,
            ciudad=ciudad,
            direccion=direccion,
        )

        messages.success(request, 'Sucursal registrada correctamente.')

        return redirect('empresas:sucursal')

    return render(request, 'forms/crear_sucursal.html')


@login_required
def listar_empleados(request):

    return render(request, 'views/listar_empleados.html')


@login_required
def registrar_empleados(request):

    empresa = Empresas.objects.filter(usuario_id=request.user)
    roles = Roles.objects.all().exclude(
    codigo=Roles.Tipos.SUPERUSUARIO
    )

    print(f"roles {roles}")


    contexto = {'empresas':empresa , 'roles':roles}
    

    if request.method == 'POST':

        nombre_empleado = request.POST.get('nombre_empleado')
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        cargo = request.POST.get('cargo')
        sucursal = request.POST.get('sucursal')
        salario = request.POST.get('salario')
        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():

            messages.error(request, 'El usuario ya existe.')

        else:

            User.objects.create_user(
                username=username,
                email=correo,
                password=password
            )

            Empleados.objects.create(
                empresa=empresa,
                nombre_empleado=nombre_empleado,
                cargo=cargo,
                sucursal_id=sucursal,
                salario=salario
            )

            messages.success(request, 'Empleado registrado correctamente.')

            return redirect('empresas:listar_empleados')

    return render(request, 'forms/registrar_empleados.html', contexto)


def asig_permisos(request):
    return render(request,'views/modulos_permisos.html')