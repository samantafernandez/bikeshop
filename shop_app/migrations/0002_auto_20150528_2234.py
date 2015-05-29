# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='current_cost',
            field=models.DecimalField(null=True, verbose_name=b'costo', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='current_sell_price',
            field=models.DecimalField(null=True, verbose_name=b'precio', max_digits=10, decimal_places=2, blank=True),
        ),
    ]
