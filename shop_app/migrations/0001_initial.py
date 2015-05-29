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
            name='Invoice',
            fields=[
                ('number', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(blank=True, to='shop_app.Customer', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('qty', models.IntegerField()),
                ('cost', models.DecimalField(max_digits=10, decimal_places=2)),
                ('invoice', models.ForeignKey(to='shop_app.Invoice')),
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
                ('code', models.CharField(max_length=10, serialize=False, verbose_name=b'codigo', primary_key=True)),
                ('description', models.CharField(max_length=500, null=True, verbose_name=b'descripcion', blank=True)),
                ('stock', models.IntegerField(default=0)),
                ('sellable', models.BooleanField(default=True)),
                ('is_service', models.BooleanField(default=False, verbose_name=b'servicio')),
                ('registered', models.BooleanField(default=False, verbose_name=b'comercializable')),
                ('current_sell_price', models.DecimalField(null=True, verbose_name=b'precio', max_digits=4, decimal_places=2, blank=True)),
                ('current_cost', models.DecimalField(null=True, verbose_name=b'costo', max_digits=4, decimal_places=2, blank=True)),
                ('imported_description', models.CharField(max_length=255, null=True, verbose_name=b'Otra descripcion', blank=True)),
                ('weelsize', models.IntegerField(null=True, blank=True)),
                ('brand', models.ForeignKey(blank=True, to='shop_app.Brand', null=True)),
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
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15, verbose_name=b'fuente')),
            ],
            options={
                'verbose_name': 'fuente',
                'verbose_name_plural': 'fuentes',
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
            name='source',
            field=models.ForeignKey(blank=True, to='shop_app.Source', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(related_name='subcategory', verbose_name=b'subcategoria', blank=True, to='shop_app.Category', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, to='shop_app.Type', null=True),
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
            model_name='invoiceitem',
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
