from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'contact/', include('contact.urls')),
        url(r'^', include('contact.urls')),
     
]
