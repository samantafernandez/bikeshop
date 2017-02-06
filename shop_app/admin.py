from django.contrib import admin

from django.forms import ModelForm, TextInput

from models import *
# Register your models here.
# from django.forms import TextInput, Textarea
# 


# 
class PriceAdmin(admin.StackedInline):
    model = Price
    extra = 1
 
class ProductForm(ModelForm):
     
    class Meta:
        widgets = {
            'code': TextInput(attrs={'class': 'input-mini'}),
            'description': TextInput(attrs={'class':'input-xxlarge'}),
            'current_sell_price': TextInput(attrs={'class':'input-mini'})
        }
        model = Product
        fields = "__all__" 
 
class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceAdmin]
    form = ProductForm
    search_fields = ('code','provider_code','manufacturer_code','description')
    list_filter = ('category','subcategory','code')
    fieldsets = (
        (None, { 'fields': (
           'code','provider_code','description', 'category', 'subcategory',
           'brand','type',
           'stock','current_sell_price',
           'is_service',
            
           )
        }),
        ('Proveedor', {
            'classes': ('collapse',),
            'fields': ('current_cost',)
        }),
        ('Imagen', {
            'classes': ('collapse',),
            'fields': ('img',)
        }),
    )
    readonly_fields = ['img']
    list_display = ('id','category','subcategory', 'code','provider_code','description','stock','current_sell_price')
    list_editable = ('current_sell_price','description')
     
    def suit_cell_attributes(self, obj, column):
        if column == 'description':
            return {'class': 'input-xxlarge'}
        if column in ['subcategory','category']:
            return {'class': 'input-medium'}
        if column in ['current_sell_price']:
            return {'class':'input-mini'}
         
        return {'class': 'input-large'}
 
     
    def img(self, obj):
        return obj.get_img()
 
    img.allow_tags = True
    img.short_description = 'Imagen'
     
     
     
    
 
     
admin.site.register(Currency)
admin.site.register(Product, ProductAdmin)

admin.site.register(Provider)
admin.site.register(Bike)
admin.site.register(Brand)
admin.site.register(Type)

admin.site.register(Category)
admin.site.register(Customer)
