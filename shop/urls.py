from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/importer/$', 'shop_app.views.import_products'),
    url(r'^admin/quote/$', 'shop_app.views.quote'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bikeshop/', include('shop_app.urls')),
    url(r'^home/', 'shop_app.views.home'),
    url(r'^quotes_main/', 'shop_app.views.quotes_main'),
    url(r'^quotes_edit/', 'shop_app.views.quotes_edit'),
    
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.STATIC_URL, 'show_indexes': True}),
    

]
