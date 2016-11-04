from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class AuthenticationConfig(ModuleMixin, AppConfig):
    name = 'authentication'
    icon = '<i class="material-icons">lock</i>'