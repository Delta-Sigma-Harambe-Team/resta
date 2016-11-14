from __future__ import unicode_literals
# Create your models here.
from django.db import models

class Resource(models.Model):
    name   = models.CharField(max_length=140, blank=False)          
    amount = models.DecimalField(max_digits = 10, decimal_places=2, blank=False,verbose_name='Cantidad en gramos') #Total en gramos
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date   = models.DateTimeField(blank = True)     #Debe ser mayor a la fecha en la que se crea

    def __unicode__(self):
        return '{0}'.format(self.content)

    def __unicode__(self):
        return '%s En Stock: %sg'%(self.name,self.amount)