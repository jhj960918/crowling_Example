from django.contrib import admin
from .models import lotteData, CustomUser, CartItem
# Register your models here.

admin.site.register(lotteData)
admin.site.register(CustomUser)
admin.site.register(CartItem)