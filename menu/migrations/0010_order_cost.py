# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20161115_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Costo de la Orden'),
        ),
    ]
