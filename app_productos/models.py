from django.db import models


# Modelo para los productos de Pokémon TCG
class Producto(models.Model):
    # ID_producto es un identificador de producto único definido por el negocio.
    # Django sigue usando 'id' como primary key automáticamente.
    ID_producto = models.PositiveIntegerField(unique=True)
    Nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50) # Ejemplo: 'Carta', 'Caja', 'Mazo', 'Suministro'
    # DecimalField es el tipo de campo recomendado para manejar dinero.
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2) 
    stock = models.PositiveIntegerField()
    id_expansion = models.PositiveIntegerField() # ID de la expansión de Pokémon a la que pertenece

    def __str__(self):
        """Representación en cadena del objeto Producto."""
        return f'Producto: {self.Nombre} (Tipo: {self.tipo}) - Expansión {self.id_expansion}'

    class Meta:
        # Nombres descriptivos para el administrador de Django
        verbose_name = "Producto de Pokémon"
        verbose_name_plural = "Productos de Pokémon"
