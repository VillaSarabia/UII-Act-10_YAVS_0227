from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    """Formulario basado en el modelo Producto para operaciones CRUD."""
    class Meta:
        model = Producto
        fields = ['ID_producto', 'Nombre', 'tipo', 'precio_venta', 'stock', 'id_expansion']
        labels = {
            'ID_producto': 'ID Producto',
            'Nombre': 'Nombre del Producto',
            'tipo': 'Tipo (Carta, Caja, Mazo, etc.)',
            'precio_venta': 'Precio de Venta ($)',
            'stock': 'Stock Disponible',
            'id_expansion': 'ID de Expansión (Saga Pokémon)',
        }
        widgets = {
            'ID_producto': forms.NumberInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            # Usamos step='0.01' para facilitar la entrada de decimales en el navegador
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_expansion': forms.NumberInput(attrs={'class': 'form-control'}),
        }