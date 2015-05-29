# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from shop_app.importer import ProductImporter

from shop_app.forms import FileForm

def importer(request):
    return render_to_response(
        "importer.html",
        {},
        RequestContext(request, {}),
    )

def list_products(request):
    # Handle file upload
    products = []
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['docfile']
            
            importer = ProductImporter()
            
            products =  importer.import_data(None, 0.15, docfile)
            
            for p in products:
                p.save()
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
    