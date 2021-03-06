from __future__ import unicode_literals

from django.db import models

from authentication.models import Account
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

    def __unicode__(self):
        return self.name

    def isAvailable(self):
        query = ResourceRecipe.objects.filter(recipe=self)
        for item in query: #Nos devuelve un ResourceRecipe
            print item.amount
            print item.ingredient
            item.red()
        return item.availability

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
    cost = models.DecimalField(max_digits = 30,decimal_places=2,default=0.0,verbose_name='Costo del combo')
    recipes = models.ManyToManyField(Recipe, through='ComboRecipe',blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

class ComboRecipe(models.Model):
    """
    Description: Relacion entre un platillo y un combo
    """
    combo = models.ForeignKey(Combo,null=False,blank=False)
    recipe = models.ForeignKey(Recipe,null=False,blank=False)    
    
    def __unicode__(self):
        return '%s %s'%(self.combo,self.recipe)

class Table(models.Model):
    waiter = models.ForeignKey(Account,null = False, blank = False)

    def __unicode__(self):
        return '#%s By %s'%(self.id,self.waiter.first_name)

ACTIVE,FINISHED,WAITING = 0,1,2
STATUS_CHOICES = ((ACTIVE, "Active"),(FINISHED, "Finished"),(WAITING,"Pending"))  
STATUS_CODES = {"Active":ACTIVE,'Finished':FINISHED,"Pending":WAITING}

PAYMENT_STATUS = ((ACTIVE, "Success"),(FINISHED, "Failed"))
PAYMENT_CODES = {'Success':ACTIVE,"Failed":FINISHED}

PAYMENT_METHODS = ((ACTIVE, "Efectivo"),(FINISHED, "Debito"))
PAYMENT_CODES = {"Efectivo":ACTIVE,'Debito':FINISHED}

class Order(models.Model):
    """
    Description: Relaciona Order
    """
    cost = models.DecimalField(max_digits = 30,decimal_places=2,default=0.0,verbose_name='Costo de la Orden')
    recipes = models.ManyToManyField(Recipe, through='OrderRecipe',blank=True)
    combo = models.ManyToManyField(Combo, through='OrderMenu',blank=True)
    table = models.ForeignKey(Table, blank=False,null=False)
    status = models.IntegerField(choices=STATUS_CHOICES,default=WAITING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s $%s'%(self.table,self.cost)

    
class OrderRecipe(models.Model):
    """
    Description: Relacion Order con platillo
    """
    order = models.ForeignKey(Order,null=False,blank=False)
    recipe = models.ForeignKey(Recipe,null=False,blank=False) 
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderMenu(models.Model):
    order = models.ForeignKey(Order,null=False,blank=False)
    combo = models.ForeignKey(Combo,null=False,blank=False) 
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    """
    Description: Payment Description
    """
    order = models.ForeignKey(Order,null=True,blank=False)
    amount = models.DecimalField(max_digits = 30,decimal_places=2,default=0.0,verbose_name='Monto pagado')
    method = models.IntegerField(choices=PAYMENT_METHODS,default=ACTIVE)
    status = models.IntegerField(choices=PAYMENT_STATUS,default=ACTIVE)

    def __unicode__(self):
        return '%s Pending: %s Paid: %s'%(self.order,self.order.cost,self.amount)
'''
Cuando la orden se pasa a activo se debe restar de almacen, si se modifica un pago que no actualice 
'''

@receiver(post_save,sender=OrderMenu) 
def PostSave_OrderMenu(sender,instance,*args, **kwargs):
    i_order = instance.order 
    i_order.cost = float(i_order.cost) + float(instance.combo.cost*instance.amount)
    i_order.save()

@receiver(post_delete,sender=OrderMenu) 
def PostDelete_OrderMenu(sender,instance,*args, **kwargs):
    i_order = instance.order 
    i_order.cost = float(i_order.cost) - float(instance.combo.cost*instance.amount)
    i_order.save()

@receiver(post_save,sender=OrderRecipe) 
def PostSave_OrderRecipe(sender,instance,*args, **kwargs):
    i_order = instance.order 
    i_order.cost = float(i_order.cost)+float(instance.recipe.amount*instance.amount)
    i_order.save()

@receiver(post_delete,sender=OrderRecipe) 
def PostDelete_OrderRecipe(sender,instance,*args, **kwargs):
    if instance.recipe.isAvailable():
        print 'ESTA DISPONIBLE'

    i_order = instance.order 
    i_order.cost = float(i_order.cost) - float(instance.recipe.amount*instance.amount)
    i_order.save()

@receiver(pre_save,sender=Payment) #No podemos agregar pagos a una orden cancelada 
def PreSave_Payment(sender,instance,*args, **kwargs):
    if instance.order.status == WAITING:
        raise Exception("Debe estar en status activo la orden")
    if instance.order.status == FINISHED:
        raise Exception("No se pueden agregar pagos a una orden finalizada")
            
@receiver(post_save,sender=Payment) #Si hacen un update de un pago no servira mas 
def PostSave_Payment(sender,instance,*args, **kwargs):
    related_order = instance.order
    related_order.cost = float(related_order.cost)-float(instance.amount)
    if related_order.cost <= 0: #Si ya no requiere mas pagos updatear a finished
        related_order.status = FINISHED
    related_order.save()
'''
area = 1 #1 is bar
for i in Order.objects.filter(status=0):#Activas
    for r in i.combo.all():
        for j in r.recipes.all():
            print j 
    for r in i.recipes.all(): 
        if r.area == area:
            print r
'''
