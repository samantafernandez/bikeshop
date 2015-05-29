from django.contrib import admin



from models import *
# Register your models here.
from django.forms import TextInput, Textarea


class PriceAdmin(admin.StackedInline):
    model = Price
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [PriceAdmin]
    search_fields = ('code', 'description')
    list_filter = ('category','subcategory','code')
    fieldsets = (
        (None, { 'fields': (
           'code','description', 'category', 'subcategory',
           'brand','type','source',''
           'stock','current_sell_price','current_cost',
           'is_service','registered',
           'imported_description',
           
           )
        }),
        ('Imagen', {
            'classes': ('collapse',),
            'fields': ('img',)
        }),
    )
    readonly_fields = ['img']
    list_display = ('code', 'description','stock','current_sell_price')
    
    def img(self, obj):
        return obj.get_img()
    
    img.allow_tags = True
    img.short_description = 'Imagen'
    

    
admin.site.register(Currency)
admin.site.register(Product, ProductAdmin)
admin.site.register(Provider)
admin.site.register(Bike)
admin.site.register(Brand)

admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Category)
admin.site.register(Customer)
