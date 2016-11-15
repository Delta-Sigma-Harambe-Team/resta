# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_auto_20161115_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Success'), (1, 'Failed')], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Active'), (1, 'Finished'), (2, 'Pending')], default=0),
        ),
    ]
