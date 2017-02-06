# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from shop_app.importer import ProductImporter
from models import Quote

from shop_app.forms import FileForm

def importer(request):
    return render_to_response("importer.html", {}, RequestContext(request, {}),     )

def home(request):
    return render_to_response("home.html", {}, RequestContext(request, {}),    )
    
def quotes_main(request):
    if request.method == 'GET':
        quotes = Quote.objects.all().order_by("-date")
        return render_to_response("quotes_main.html", {"quotes" : quotes}, RequestContext(request, {}),)

def quotes_edit(request):
    return render_to_response(
        "quotes_edit.html",
        {},
        RequestContext(request, {}),
    )

def import_products(request):
    # Handle file upload
    products = []
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['docfile']
            
            importer = ProductImporter()
            
            products =  importer.import_data(None, docfile)
            
            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('shop_app.views.list_products'))
            return render_to_response(
                                      'import_result.html',
                                      {'products': products, 'form': form},
                                      context_instance=RequestContext(request)
                                      ) 
        
    else:
        form = FileForm() # A empty, unbound form


    return render_to_response('import_result.html',
                                      {'products': products, 'form': form},
                                      context_instance=RequestContext(request))

    # Render list page with the documents and the form
    
def quote(request):
    return render_to_response(
                                      'quote.html',
                                     
                                      context_instance=RequestContext(request)
                                      ) 
    
    