from django.contrib import admin
from .models import *

class TermInlineAdmin(admin.StackedInline): # TabularInline
    model = Recipe.item.through
    extra=0

class ComboRecipeInLine(admin.StackedInline): # TabularInline
    model = Combo.recipes.through
    extra=0

class OrderCombosInline(admin.StackedInline): # TabularInline
    model = Order.recipes.through
    extra=0
class OrderRecipeInline(admin.StackedInline): # TabularInline
    model = Order.combo.through
    extra=0

class CurrentOrdersInLine(admin.StackedInline):
    model = Table
    extra = 0

@admin.register(Recipe)
class AdminOrder(admin.ModelAdmin):
    icon = '<i class="material-icons">kitchen</i>'
    list_display = ('name','preparation_time','area' ,'amount','created_at','updated_at')
    list_filter = ('preparation_time','name')
    inlines = (TermInlineAdmin,)

@admin.register(Combo)
class AdminCombo(admin.ModelAdmin):
    icon = '<i class="material-icons">local_dining</i>'
    list_display = ('name',)
    list_filter = ('name',)

    inlines = (ComboRecipeInLine,)

@admin.register(Order)
class AdminCombo(admin.ModelAdmin):
    icon = '<i class="material-icons">receipt</i>'
    list_display = ('id','status','table')
    list_filter = ('status',)
    readonly_fields=('cost','status',)
    
    inlines = (OrderCombosInline,OrderRecipeInline,)

@admin.register(Table)
class AdminTable(admin.ModelAdmin):
    icon = '<i class="material-icons">room_service</i>'

@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    icon = '<i class="material-icons">payment</i>'
