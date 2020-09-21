from django.contrib import admin
from .models import musinsaData, CustomUser, CartItem
# Register your models here.

admin.site.register(musinsaData)
admin.site.register(CustomUser)
admin.site.register(CartItem)