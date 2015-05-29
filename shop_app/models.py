from django.db import models
from pydoc import describe
from pip._vendor.requests.packages.chardet.chardetect import description_of
from test.test_imageop import MAX_LEN
from django.db.models.fields import CharField

# Create your models here.


class Category(models.Model):
    name = models.CharField('categoria', max_length=30)
    
    def __str__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

class Type(models.Model):
    name = models.CharField('tipo', max_length=15)
    
    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'

class Source(models.Model):
    name = models.CharField('fuente', max_length=15)
    
    class Meta:
        verbose_name = 'fuente'
        verbose_name_plural = 'fuentes'
    

class Brand(models.Model):
    name = models.CharField('marca', max_length=250)
    
    def __str__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        

class Material(models.Model):
    name = models.CharField('material', max_length=250)
    
    def __str__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiales'

class Product(models.Model):
    code = models.CharField('codigo', max_length=10, primary_key=True)
    description = models.CharField('descripcion', max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name='categoria')
    subcategory = models.ForeignKey(Category, null=True, blank=True, verbose_name='subcategoria', related_name='subcategory')
    type = models.ForeignKey(Type, null=True, blank=True)
    stock = models.IntegerField(default=0)
    sellable = models.BooleanField(default=True)
    is_service = models.BooleanField('servicio', default=False)
    registered = models.BooleanField('comercializable', default=False)
    current_sell_price = models.DecimalField('precio', decimal_places=2,max_digits=10,  null=True, blank=True)
    current_cost = models.DecimalField('costo', decimal_places=2,max_digits=10,  null=True, blank=True)
    imported_description = models.CharField('Otra descripcion', max_length=255,  null=True, blank=True)
    brand = models.ForeignKey(Brand,  null=True, blank=True)
    source = models.ForeignKey(Source,   null=True, blank=True)
    material = models.ForeignKey(Material,  null=True, blank=True)
    weelsize = models.IntegerField(null=True, blank=True)
                
    def __str__(self):          
        return self.code + " - " + self.description
    
  
    def get_img(self):
        return u'<img src="http://www.bicicleteriapereyra.com.ar/uploads/fotos_productos/%s-01.jpg" />' % self.code
   
   
        
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

       
    
class Currency(models.Model):
    name = models.CharField(max_length=30)
    exchange_rate = models.DecimalField(decimal_places=2,max_digits=4)
    
    def __str__(self):          
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
    
    
    def __str__(self):          
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
    
    def __str__(self):          
        return self.name
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


   
    
class Bike(models.Model):
    
    description = models.CharField('descripcion', max_length=500)
    owner = models.ForeignKey(Customer, verbose_name= 'propietario')
    brand = models.ForeignKey(Brand, null=True, blank=True, verbose_name='Marca')
    year = models.IntegerField('modelo', null=True, blank=True)
    
    def __str__(self):          
        return self.owner.name + "-" + self.description + self.brand.name + self.year
    
    class Meta:
        verbose_name = 'Bici'
        verbose_name_plural = 'Bicis'

    
class Invoice(models.Model):
    number = models.IntegerField(primary_key=True)
    date = models.DateField()
    customer = models.ForeignKey(Customer,  null=True, blank=True)
    
    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    qty = models.IntegerField()
    product = models.ForeignKey(Product,null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    