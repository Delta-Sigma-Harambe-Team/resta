from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class ProductsConfig(ModuleMixin, AppConfig):
    name = 'products'
    icon = '<i class="material-icons">shopping_cart</i>'