from django.contrib import admin
from .models import *

class TermInlineAdmin(admin.StackedInline): # TabularInline
    model = Recipe.item.through
    extra=0

class ComboRecipeInLine(admin.StackedInline): # TabularInline
    model = Combo.recipes.through
    extra=0

# Register your models here.
@admin.register(ResourceRecipe)
class AdminOrderItem(admin.ModelAdmin):
    icon = '<i class="material-icons">http</i>'
    list_display = ('recipe', 'ingredient','amount')
    list_filter = ('recipe','amount')

@admin.register(Recipe)
class AdminOrder(admin.ModelAdmin):
    icon = '<i class="material-icons">dns</i>'
    list_display = ('name','preparation_time','area' ,'amount','created_at','updated_at')
    list_filter = ('preparation_time','name')
    #readonly_fields=('amount',)
    inlines = (TermInlineAdmin,)

@admin.register(Combo)
class AdminCombo(admin.ModelAdmin):
    icon = '<i class="material-icons">dns</i>'
    list_display = ('name',)
    list_filter = ('name',)

    inlines = (ComboRecipeInLine,)
    