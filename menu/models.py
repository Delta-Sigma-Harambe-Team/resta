from __future__ import unicode_literals

from django.db import models

from products.models import Resource
from django.db.models.signals import post_save, post_delete , pre_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry

COCINA,BAR = 0,1
STATUS_CHOICES = {"Cocina":COCINA,'Bar':BAR}
STATUS_CODES = ((COCINA, "Cocina"),(BAR, "Bar"))  
# Create your models here.
class Recipe(models.Model): 
    name = models.CharField(max_length=140,blank=False)          
    
    preparation_time = models.IntegerField(blank=False,verbose_name='Min de preparacion')   
    area = models.IntegerField(choices=STATUS_CODES,default=COCINA)

    amount = models.DecimalField(max_digits = 30,decimal_places=2,default=0.0,verbose_name='Costo del platillo')

    item = models.ManyToManyField(Resource, through='ResourceRecipe',blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ResourceRecipe(models.Model):
    recipe = models.ForeignKey(Recipe,null=False,blank=False)
    ingredient = models.ForeignKey(Resource,null=False,blank=False)    
    amount = models.DecimalField(max_digits = 10, decimal_places=2, blank=False,verbose_name='Cantidad en gramos')

    def __unicode__(self):
        return '%s %s %s'%(self.recipe,self.ingredient, self.amount)

class Combo(models.Model):
    """
    Description: Paquete que tiene multiples platillos
    """
    name   = models.CharField(max_length=140, blank=False)          
    
    recipes = models.ManyToManyField(Recipe, through='ComboRecipe',blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return name

class ComboRecipe(models.Model):
    """
    Description: Relacion entre un platillo y un combo
    """
    combo = models.ForeignKey(Combo,null=False,blank=False)
    recipe = models.ForeignKey(Recipe,null=False,blank=False)    
    
    def __unicode__(self):
        return '%s %s'%(self.combo,self.recipe)
    