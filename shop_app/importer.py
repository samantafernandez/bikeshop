import csv
from models import Category
from models import Product
from models import Source

from django.conf import settings

import sys, getopt




class ProductImporter():
    def get_category(self, category_name):
        category = None
        if category_name != None:
            try:
                category = Category.objects.get(pk=category_name)
            except Category.DoesNotExist:
                    category = Category(category_name)
                    category.save()
             
        return category
    
    def get_source(self, source_name):
        source = None
        if source_name != None:
            try:
                source = Source.objects.get(pk=source_name)
            except Source.DoesNotExist:
                source = Source(source_name)
                source.save()
        return source
    
    def import_product(self, category_name, subcategory_name, code, description, list_price, brand, discount, source, qty):
        if(code != None):
            category = self.get_category(category_name)
            subcategory = self.get_category(subcategory_name)
            
                          
            net_price = list_price #- list_price * discount
            
            try:
                product = Product.objects.get(pk=code)
            except Product.DoesNotExist:
                product = Product(code=code, description=description,category=category, subcategory=subcategory, current_cost=net_price, source=source)
    
        product.current_cost = net_price
        product.stock = product.stock + int(qty)
        return product
            
    
    def import_data(self, source_name, discount, source_file):
        
        products = []
        with source_file as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                code = row[0]
                description = row[1]
                qty = row[2]
                list_price = row[3]
                
                product = self.import_product(None, None, code, description, list_price, None, discount, source_name,qty)
                
                products.append(product)
                
        return products
    
    

if __name__ == '__main__':
    settings.configure()
    importer = ProductImporter() 

    print sys.argv[1:] 
            
       
         