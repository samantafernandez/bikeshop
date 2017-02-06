import csv
from models import Category
from models import Product
from models import Subcategory
from decimal import Decimal

from django.conf import settings

import sys, getopt




class ProductImporter():
    def get_category(self, category_name):
        category = None
        if category_name != None:
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                    category = Category()
                    category.name = category_name
                    category.save()
             
        return category
    
    def get_subcategory(self, category_name, subcategory_name):
        category = None
        subcategory = None
        if category_name != None:
            try:
                category = Category.objects.get(name = category_name)
                if category != None:
                        subcategory = Subcategory.objects.get(name=subcategory_name, category = category)
                        
                        
            except Category.DoesNotExist:
                category = Category(name=category_name)
                category.save()
                    
                subcategory = Subcategory(category=category, name=subcategory_name)
                subcategory.save()
                    
            except Subcategory.DoesNotExist:
                subcategory = Subcategory(category=category, name=subcategory_name)
                subcategory.save()
                
             
        return subcategory

    
    def import_product(self, category_name, subcategory_name, code, provider_code, description, sell_price, stock,
                        list_cost, net_cost ):
        product = None
        if(description != None and description != ""):
            category = self.get_category(category_name)
            subcategory = self.get_subcategory(category_name, subcategory_name)
            
            
            if net_cost is None:
                net_cost = list_cost
            
            try:
                
                product = Product.objects.get(description=description )
            except Product.DoesNotExist:
                product = Product(code=code, provider_code = provider_code, description=description,category=category, 
                                  subcategory=subcategory)
    
            try:
                product.current_cost = Decimal(net_cost)
            except:
                pass
        
            try:
                product.current_sell_price = Decimal(sell_price)
            except:
                pass
        
            try:
                product.stock =  int(stock)
            except:
                pass
            
            if product != None:
                product.save()
        return product
            
    
    def import_data(self, source_name, source_file):
        
        products = []
        with source_file as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                category = row[0]
                subcategory = row[1]
                code= row[2]
                provider_code = row[3]
                description = row[4]
                list_price = row[5]
                stock = row[6]
                list_cost = row[8]
                net_cost = row[9]
                
                if provider_code != '0':
                    product = self.import_product(category, subcategory, code, provider_code, description, list_price, stock,
                                               list_cost, net_cost)
                
                    if product != None:
                        products.append(product)
                
        return products
