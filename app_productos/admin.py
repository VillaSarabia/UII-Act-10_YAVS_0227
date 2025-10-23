from django.contrib import admin
from .models import Producto

# Registrar el nuevo modelo Producto en la interfaz de administración de Django
admin.site.register(Producto)
