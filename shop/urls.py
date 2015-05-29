from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/importer/$', 'shop_app.views.importer'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bikeshop/', include('shop_app.urls')),
   

]
