from django.urls import path
from . import views

urlpatterns = [
    # Ruta principal para listar todos los productos
    path('', views.index, name='index'),
    # Ruta para ver un producto específico por su ID (primary key de Django)
    path('<int:id>', views.view_producto, name='view_producto'),
    # Ruta para el formulario de adición
    path('add/', views.add, name='add'),
    # Ruta para el formulario de edición, requiere el ID del producto
    path('edit/<int:id>/', views.edit, name='edit'),
    # Ruta para eliminar un producto, requiere el ID
    path('delete/<int:id>/', views.delete, name='delete'),
]
