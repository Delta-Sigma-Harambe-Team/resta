from __future__ import unicode_literals
from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class MenuConfig(ModuleMixin, AppConfig):
    name = 'menu'
    icon = '<i class="material-icons">shopping_cart</i>'