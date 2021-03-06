# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_order_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=30, verbose_name='Monto pagado')),
                ('method', models.IntegerField(choices=[(0, 'Efectivo'), (1, 'Debito')], default=0)),
            ],
        ),
    ]
