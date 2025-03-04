from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    #path('donations/', include('donations.urls')),
    #path('charities/', include('charities.urls')),
]
