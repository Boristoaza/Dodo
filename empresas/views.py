from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Empresas,Sucursales , Empleados
from usuarios.models import Cargos_laborales
from django.contrib.auth.models import User 
from django.contrib import messages

@login_required
def empresa_view(request):
    return render(request,'views/empresa.html')

@login_required
def sucursal_view(request):
    return render(request,'views/sucursal.html')

@login_required
def crear_sucursal_view(request):

    print(request.user.username)
    if request.method == 'POST':
        nombre_sucursal = request.POST.get('nombre_sucursal')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')

        empresa = request.user.empresa

        crear_sucursal = Sucursales.objects.create(
            empresa=empresa,
            nombre_sucursal=nombre_sucursal,
            telefono=telefono,
            ciudad=ciudad,
            direccion=direccion,
        )
        messages.success(request, 'Sucursal registrada correctamente.')

    return render(request,'forms/crear_sucursal.html')

@login_required
def listar_empleados(request):
    cargos_laborales = Cargos_laborales.Cargos.choices

    usuario = User.objects.filter(username=request.user).first()
    empresa = Empresas.objects.filter(usuario=usuario).first()
    sucursal = Sucursales.objects.filter(empresa=empresa).all()
    empleados = Empleados.objects.select_related('sucursal')

    contexto = {'empleados':empleados,'sucursales':sucursal, 'cargos': cargos_laborales,}
    return render(request,'views/listar_empleados.html',contexto)

@login_required
def registrar_empleados(request):

    empresa = Empresas.objects.get(usuario=request.user)

    cargos_laborales = Cargos_laborales.Cargos.choices

    sucursales = Sucursales.objects.filter(empresa=empresa)

    contexto = {
        'cargos': cargos_laborales,
        'sucursales': sucursales,
    }



    if request.method == 'POST':

        nombre_empleado = request.POST.get('nombre_empleado')
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        cargo = request.POST.get('cargo')
        sucursal = request.POST.get('sucursal')
        salario = request.POST.get('salario')
        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():
            print('El usuario ya existe')

        else:
            crear_empleado = User.objects.create_user(
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

    return render(request, 'forms/registrar_empleados.html',contexto)

# @login_required
# def registrar_empresa_view(request):
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