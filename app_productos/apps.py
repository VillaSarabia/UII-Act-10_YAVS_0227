from django.apps import AppConfig


class AppProductoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # CORRECCIÓN: El nombre del módulo debe coincidir con el nombre de la carpeta
    name = 'app_productos' 
    verbose_name = 'Productos Pokémon'
