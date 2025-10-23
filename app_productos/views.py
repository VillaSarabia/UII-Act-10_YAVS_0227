from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Producto
from .forms import ProductoForm


def index(request):
    """Muestra la lista de todos los productos."""
    # Los productos se cargan y se ordenan para una mejor visualización
    productos = Producto.objects.all().order_by('id_expansion', 'Nombre')
    return render(request, 'productos/index.html', {
        'productos': productos
    })


def view_producto(request, id):
    """Muestra detalles de un producto específico (redirige al índice por defecto)."""
    # Usamos get_object_or_404 para manejar si el producto no existe
    producto = get_object_or_404(Producto, pk=id)
    # Aquí puedes renderizar un template de detalle si lo creas.
    # return render(request, 'productos/view.html', {'producto': producto})
    return HttpResponseRedirect(reverse('index'))


def add(request):
    """Permite agregar un nuevo producto."""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # CORRECCIÓN: Al usar ModelForm, solo necesitamos llamar a .save()
            form.save()
            # Redirigir al índice después de una adición exitosa
            return HttpResponseRedirect(reverse('index'))
    else:
        # Crear un formulario vacío para el método GET
        form = ProductoForm()

    # Se asume que el template está en 'productos/add.html'
    return render(request, 'productos/add.html', {
        'form': form
    })


def edit(request, id):
    """Permite editar un producto existente."""
    # Obtener la instancia del producto o lanzar 404
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        # Instanciar el formulario con los datos POST y la instancia a modificar
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            # Mostrar la página de edición con mensaje de éxito
            return render(request, 'productos/edit.html', {
                'form': form,
                'success': True # Variable para mostrar un mensaje en el template
            })
    else:
        # Llenar el formulario con los datos de la instancia existente (GET)
        form = ProductoForm(instance=producto)

    # Se asume que el template está en 'productos/edit.html'
    return render(request, 'productos/edit.html', {
        'form': form
    })


def delete(request, id):
    """Permite eliminar un producto y redirige al índice."""
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        producto.delete()
        # Redirigir al índice después de la eliminación
    return HttpResponseRedirect(reverse('index'))
