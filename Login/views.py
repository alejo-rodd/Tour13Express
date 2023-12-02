from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from django import forms

# Create your views here.
#@login_required
def index(request):
    #return render(request, 'productos/productos.html')
    return redirect('productos_cliente')

def inicio(request):
    return render(request, 'productos/productos.html')

@login_required
def salir(request):
    logout(request)
    return redirect('/')


def registrarEmprendimiento(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']

        if password and passwordConfirm and password != passwordConfirm:
            messages.error(request, 'Las contraseñas no coinciden.')
        else:
            # Crea una instancia del modelo User y guarda los datos
            nuevo_emprendimiento = User.objects.create_user(username=username, password=password)
            # Puedes mostrar un mensaje de éxito
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            # Redirige a la página de éxito o a donde desees
            return redirect('productos')
    return render(request, 'registration/login.html')

def productos_cliente(request):
    productos = Producto.objects.all()
    return render(request, 'clientes/productos_clientes.html',{
        'productos': productos
    })

def info_graffitour(request):
    return render(request, 'clientes/info.html')

@login_required
def productos(request):
    productos = Producto.objects.filter(user=request.user)
    return render(request, 'productos/productos.html', {
        'productos': productos
    })

@login_required
def crear_producto(request):  
    if request.method == 'GET':
        form = ProductoForm()
        form.fields['activo'].widget = forms.HiddenInput()
        return render(request, 'productos/crear_producto.html', {
            'form': form
        })
    else:
        try:
            form = ProductoForm(request.POST, request.FILES)
            new_producto = form.save(commit=False)
            new_producto.user = request.user  # Se le asigna el usuario a la tarea
            new_producto.save()
            
            return redirect('productos')
        except ValueError:
            return render(request, 'productos/crear_producto.html', {
                'form': ProductoForm,
                'error': 'Por favor ingresa valores válidos'
            })

@login_required
def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id, user=request.user)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/producto_detalle.html', {
            'producto': producto,
            'form': form
        })

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id, user=request.user)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')


