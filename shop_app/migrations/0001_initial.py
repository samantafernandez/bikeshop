# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=500, verbose_name=b'descripcion')),
                ('year', models.IntegerField(null=True, verbose_name=b'modelo', blank=True)),
            ],
            options={
                'verbose_name': 'Bici',
                'verbose_name_plural': 'Bicis',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'marca')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'categoria')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('exchange_rate', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Moneda',
                'verbose_name_plural': 'Monedas',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name=b'apellido y nombre', blank=True)),
                ('home_phone', models.CharField(max_length=100, null=True, verbose_name=b'telefono', blank=True)),
                ('mobile_phone', models.CharField(max_length=100, null=True, verbose_name=b'celular', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('facebook', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'material')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiales',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500, null=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('qty', models.IntegerField()),
                ('order', models.ForeignKey(to='shop_app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_value', models.DecimalField(verbose_name=b'precio de lista', max_digits=10, decimal_places=2)),
                ('discount', models.DecimalField(verbose_name=b'% descuento', max_digits=10, decimal_places=2)),
                ('date_start', models.DateField(null=True, verbose_name=b'desde', blank=True)),
                ('date_end', models.DateField(null=True, verbose_name=b'hasta', blank=True)),
                ('net_value', models.DecimalField(verbose_name=b'precio neto', max_digits=10, decimal_places=2)),
                ('currency', models.ForeignKey(verbose_name=b'Moneda', blank=True, to='shop_app.Currency', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name=b'codigo', blank=True)),
                ('manufacturer_code', models.CharField(max_length=20, verbose_name=b'codigo de fabrica', blank=True)),
                ('provider_code', models.CharField(max_length=20, verbose_name=b'codigo del proveedor', blank=True)),
                ('photo_code', models.CharField(max_length=19, blank=True)),
                ('description', models.CharField(max_length=500, null=True, verbose_name=b'descripcion', blank=True)),
                ('stock', models.IntegerField(default=0, verbose_name=b'stock')),
                ('min_stock', models.IntegerField(default=0, verbose_name=b'stock minimo')),
                ('purchase_qty', models.IntegerField(default=0, verbose_name=b'cantidad de reposicion')),
                ('sellable', models.BooleanField(default=True, verbose_name=b'de venta al publico')),
                ('is_service', models.BooleanField(default=False, verbose_name=b'servicio')),
                ('current_sell_price', models.DecimalField(null=True, verbose_name=b'precio', max_digits=10, decimal_places=2, blank=True)),
                ('current_cost', models.DecimalField(null=True, verbose_name=b'costo', max_digits=10, decimal_places=2, blank=True)),
                ('imported_description', models.CharField(max_length=255, null=True, verbose_name=b'otra descripcion', blank=True)),
                ('wheelsize', models.CharField(max_length=10, null=True, verbose_name=b'rodado', blank=True)),
                ('brand', models.ForeignKey(verbose_name=b'marca', blank=True, to='shop_app.Brand', null=True)),
                ('category', models.ForeignKey(verbose_name=b'categoria', blank=True, to='shop_app.Category', null=True)),
                ('material', models.ForeignKey(blank=True, to='shop_app.Material', null=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('tel', models.CharField(max_length=100, null=True, verbose_name=b'telefono', blank=True)),
                ('dir', models.CharField(max_length=100, null=True, verbose_name=b'direccion', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name=b'email', blank=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('number', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Fecha')),
                ('completed', models.BooleanField()),
                ('total', models.DecimalField(null=True, verbose_name=b'Total', max_digits=10, decimal_places=2, blank=True)),
                ('advance_payment', models.DecimalField(null=True, verbose_name=b'Adelanto', max_digits=10, decimal_places=2, blank=True)),
                ('handover', models.DateField(null=True, verbose_name=b'Fecha Entrega', blank=True)),
                ('customer', models.ForeignKey(blank=True, to='shop_app.Customer', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500, null=True)),
                ('price', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('qty', models.IntegerField(null=True)),
                ('cost', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('product', models.ForeignKey(to='shop_app.Product', null=True)),
                ('quote', models.ForeignKey(to='shop_app.Quote')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'subcategoria')),
                ('category', models.ForeignKey(verbose_name=b'categoria', to='shop_app.Category')),
            ],
            options={
                'verbose_name': 'subcategoria',
                'verbose_name_plural': 'subcategorias',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15, verbose_name=b'tipo')),
            ],
            options={
                'verbose_name': 'tipo',
                'verbose_name_plural': 'tipos',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(related_name='subcategory', verbose_name=b'subcategoria', blank=True, to='shop_app.Subcategory', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(verbose_name=b'tipo bici', blank=True, to='shop_app.Type', null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(to='shop_app.Product'),
        ),
        migrations.AddField(
            model_name='price',
            name='provider',
            field=models.ForeignKey(verbose_name=b'Proveedor', to='shop_app.Provider'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(to='shop_app.Product', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='provider',
            field=models.ForeignKey(to='shop_app.Provider'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='product',
            field=models.ForeignKey(to='shop_app.Product', null=True),
        ),
        migrations.AddField(
            model_name='bike',
            name='brand',
            field=models.ForeignKey(verbose_name=b'Marca', blank=True, to='shop_app.Brand', null=True),
        ),
        migrations.AddField(
            model_name='bike',
            name='owner',
            field=models.ForeignKey(verbose_name=b'propietario', to='shop_app.Customer'),
        ),
    ]
