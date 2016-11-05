from django.contrib import admin
from .models import *

class TermInlineAdmin(admin.StackedInline): # TabularInline
    model = Recipe.item.through
    extra=0
# Register your models here.
@admin.register(ResourceRecipe)
class AdminOrderItem(admin.ModelAdmin):
    icon = '<i class="material-icons">code</i>'
    list_display = ('recipe', 'ingredient','amount')
    list_filter = ('recipe','amount')

@admin.register(Recipe)
class AdminOrder(admin.ModelAdmin):
    icon = '<i class="material-icons">content_paste</i>'
    list_display = ('preparation_time','area' ,'amount','created_at','updated_at')
    list_filter = ('preparation_time',)
    #readonly_fields=('amount',)
    inlines = (TermInlineAdmin,)
    