from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from register import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path("register/", v.register, name="register"),

    
]
