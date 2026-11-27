
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Empresas, Sucursales, Empleados 
from usuarios.models import Roles , Modulos




@login_required
def empresa_view(request):
    return render(request, 'views/empresa.html')


@login_required
def sucursal_view(request):
    sucursales = Sucursales.objects.all()
    empresa = Empresas.objects.filter(usuario_id=request.user)

    contexto = {'sucursales':sucursales , 'empresas':empresa}
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
    empleado = Empleados.objects.all() 
    contexto = {'empleados':empleado}
    return render(request, 'views/listar_empleados.html',contexto)


@login_required
def registrar_empleados(request):

    empresa = Empresas.objects.filter(usuario_id=request.user)


    contexto = {'empresas': empresa }

    if request.method == 'POST':

        nombre_empleado = request.POST.get('nombre_empleado')
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        sucursal = request.POST.get('sucursal')
        salario = request.POST.get('salario')
        username = request.POST.get('username')

        print("========== DATOS RECIBIDOS ==========")
        print(f"Nombre: {nombre_empleado}")
        print(f"Correo: {correo}")
        print(f"Password: {password}")
        print(f"Sucursal: {sucursal}")
        print(f"Salario: {salario}")
        print(f"Username: {username}")
        print("=====================================")

        if User.objects.filter(username=username).exists():

            messages.error(request, 'El usuario ya existe.')

        else:

            usuario = User.objects.create_user(
                username=username,
                email=correo,
                password=password
            )

            Empleados.objects.create(
                usuario=usuario,
                empresa=empresa.first(),
                nombre_empleado=nombre_empleado,
                sucursal_id=sucursal,
                salario=salario
            )

            messages.success(request, 'Empleado registrado correctamente.')

            return redirect('empresas:listar_empleados')

    return render(request, 'forms/registrar_empleados.html', contexto)


def asig_modulos_permisos(request):
    modulos = Modulos.objects.filter(estado=True)
    
    if request.method == 'POST':

        for modulo in modulos:

            modulo_activo = request.POST.get(f'modulo_{modulo.id}')

            consultar = request.POST.get(f'consultar_{modulo.id}')
            crear = request.POST.get(f'crear_{modulo.id}')
            editar = request.POST.get(f'editar_{modulo.id}')
            eliminar = request.POST.get(f'eliminar_{modulo.id}')
            aprobar = request.POST.get(f'aprobar_{modulo.id}')
            anular = request.POST.get(f'anular_{modulo.id}')
            exportar = request.POST.get(f'exportar_{modulo.id}')

            print(f'Módulo: {modulo.nombre}')
            print(f'Activo: {modulo_activo}')
            print(f'Consultar: {consultar}')
            print(f'Crear: {crear}')
            print(f'Editar: {editar}')
            print(f'Eliminar: {eliminar}')
            print(f'Aprobar: {aprobar}')
            print(f'Anular: {anular}')
            print(f'Exportar: {exportar}')
            print('---------------------------')

    contexto = {
        'modulos': modulos
    }



    return render(request,'views/modulos_permisos.html', contexto)