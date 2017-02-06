from models import Quote, QuoteItem
from datetime import date
from models import Customer
from models import Bike
from shop_app.models import Product, Price

class quoteService():
    
    def create_quote(self, customer_id, bike_id):
        quote = Quote()
        quote.date = date.today()
        
        customer = Customer.objects.get(pk=customer_id)
        bike = Bike.objects.get(pk = bike_id)
        
        quote.customer = customer
        quote.bike = bike
        return quote
    
    
    
    def add_item(self, quote_id, code, qty, price, description):
        quoteItem = QuoteItem()
        
        quote = Quote.objects.get(pk=quote_id)
        product = Product.objects.get(pk=code)
        if quote == None or product == None:
            return None
        
        quoteItem.quote = quote
        quoteItem.description = product.description
        quoteItem.code = code
        quoteItem.product = product
        quoteItem.qty = qty
        quoteItem.price = Price
        quoteItem.cost = product.cost
        
        if description != None:
            quoteItem.description = description
        
        quoteItem.save()
            
    
    def complete(self, quote_id):
        quote = Quote.objects.get(pk=quote_id)
        
        if quote != None:
            quote.complete = True
    
    
    
    
    
    
    