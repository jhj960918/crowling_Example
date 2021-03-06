"""projectname URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.crowling, name='crowling'),
    path('signin', app.views.signin, name = 'signin'),
    path('logout', app.views.logout, name = 'logout'),
    path('signup', app.views.signup, name = 'signup'),
    path('my_cart', app.views.my_cart, name = 'my_cart'),
    path('add_cart/<int:product_pk>', app.views.add_cart, name='add_cart'),
    path('delete_cart_item/<int:product_pk>', app.views.delete_cart_item, name='delete_cart_item'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
