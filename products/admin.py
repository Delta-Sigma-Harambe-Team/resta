from django.contrib import admin
from .models import Resource
# Register your models here.
@admin.register(Resource)
class AdminResource(admin.ModelAdmin):
    icon = '<i class="material-icons">shopping_basket</i>'
    list_display = ('name','amount','due_date')
    list_filter = ('name','amount','due_date')