from django.db import models

from enum import Enum
from datetime import date

class InvoiceStatus(Enum):
    draft = 1
    closed = 2
    
class Category(models.Model):
    name = models.CharField('categoria', max_length=30, unique=True)
    
    def __unicode__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
        
class Subcategory(models.Model):
    name = models.CharField('subcategoria', max_length=30)
    category = models.ForeignKey(Category, verbose_name="categoria")
    
    def __unicode__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'subcategoria'
        verbose_name_plural = 'subcategorias'
    
    

class Type(models.Model):
    name = models.CharField('tipo', max_length=15, unique=True)
    
    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'

class Brand(models.Model):
    name = models.CharField('marca', max_length=250, unique=True)
    
    def __unicode__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        

class Material(models.Model):
    name = models.CharField('material', max_length=250, unique=True)
    
    def __unicode__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiales'

class Product(models.Model):
    code = models.CharField('codigo', max_length=10, blank=True,unique=True)
    manufacturer_code = models.CharField('codigo de fabrica', max_length=20, blank=True)
    provider_code = models.CharField('codigo del proveedor', max_length=20, blank=True, unique=True)
    photo_code= models.CharField(max_length=19,blank=True)
    
    description = models.CharField('descripcion', max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name='categoria')
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, verbose_name='subcategoria', related_name='subcategory')
    
    stock = models.IntegerField('stock', default=0)
    min_stock = models.IntegerField('stock minimo', default=0)
    purchase_qty = models.IntegerField('cantidad de reposicion',default=0)
    
    sellable = models.BooleanField('de venta al publico',default=True)
    is_service = models.BooleanField('servicio', default=False)
     
    current_sell_price = models.DecimalField('precio', decimal_places=2,max_digits=10,  null=True, blank=True)
    current_cost = models.DecimalField('costo', decimal_places=2,max_digits=10,  null=True, blank=True)
    
    imported_description = models.CharField('otra descripcion', max_length=255,  null=True, blank=True)
    
    brand = models.ForeignKey(Brand,  null=True, blank=True, verbose_name='marca')
    # hierro, plastico, aluminio
    material = models.ForeignKey(Material,  null=True, blank=True)
    # bmx, mtb, ruta
    type = models.ForeignKey(Type, null=True, blank=True, verbose_name='tipo bici')
    #20, 26, 29
    wheelsize = models.CharField('rodado', max_length=10, null=True, blank=True)
                
    def __unicode__(self):          
        return self.code + " - " + self.description
    
  
    def get_img(self):
        return u'<img src="http://www.bicicleteriapereyra.com.ar/uploads/fotos_productos/%s-01.jpg" />' % self.photo_code
   
   
        
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

       
    
class Currency(models.Model):
    name = models.CharField(max_length=30)
    exchange_rate = models.DecimalField(decimal_places=2,max_digits=4)
    
    def __unicode__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'

    
class Provider(models.Model):
    name = models.CharField('nombre', max_length=100)
    tel = models.CharField('telefono', max_length=100, null=True, blank=True)
    dir = models.CharField('direccion', max_length=100,   null=True, blank=True)
    email = models.EmailField('email',  null=True, blank=True)
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    
    def __unicode__(self):          
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product)
    list_value = models.DecimalField('precio de lista', decimal_places=2,max_digits=10)
    discount = models.DecimalField('% descuento', decimal_places=2,max_digits=10)
    provider = models.ForeignKey(Provider, verbose_name = 'Proveedor')
    date_start = models.DateField('desde', null=True, blank=True)
    date_end = models.DateField('hasta', null=True, blank=True)
    net_value = models.DecimalField( 'precio neto' , decimal_places=2,max_digits=10)
    currency = models.ForeignKey(Currency,  null=True, blank=True, verbose_name= 'Moneda')
    
class Customer(models.Model):
    name = models.CharField('apellido y nombre', max_length=100,  null=True, blank=True)
    home_phone = models.CharField('telefono', max_length=100,  null=True, blank=True)
    mobile_phone = models.CharField('celular', max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


   
    
class Bike(models.Model):
    
    description = models.CharField('descripcion', max_length=500)
    owner = models.ForeignKey(Customer, verbose_name= 'propietario')
    brand = models.ForeignKey(Brand, null=True, blank=True, verbose_name='Marca')
    year = models.IntegerField('modelo', null=True, blank=True)
    
    def __unicode__(self):          
        return self.owner.name + "-" + self.description + self.brand.name + self.year
    
    class Meta:
        verbose_name = 'Bici'
        verbose_name_plural = 'Bicis'


    
class Quote(models.Model):
    number = models.IntegerField(primary_key=True)
    date = models.DateField('Fecha', )
    customer = models.ForeignKey(Customer,  null=True, blank=True)
    completed = models.BooleanField()
    total = models.DecimalField('Total', null=True, blank=True, decimal_places=2,max_digits=10)
    advance_payment = models.DecimalField('Adelanto',null=True, blank=True, decimal_places=2,max_digits=10)
    handover = models.DateField('Fecha Entrega',null=True, blank=True)
    
    
class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=500, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10, null=True)
    qty = models.IntegerField(null=True)
    product = models.ForeignKey(Product,null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    
    
    
class Order(models.Model):
    date = models.DateField()
    provider = models.ForeignKey(Provider)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    code = models.CharField(max_length=10)    
    description = models.CharField(max_length=500, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    qty = models.IntegerField()
    product = models.ForeignKey(Product,null=True)
    
    
class InventoryItem(models.Model):
    product = models.ForeignKey(Product,null=True)
    date = models.DateField()
    qty = models.IntegerField()
    
    
    
    
    
    
    
    
    
    