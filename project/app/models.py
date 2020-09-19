from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class musinsaData(models.Model):
    search_musinsa = models.TextField()#검색어 필드
    musinsaImage = models.ImageField(upload_to='images/', blank=True)# 상품 이미지
    musinsaUrl = models.TextField()# 상품 이미지 URL
    musinName = models.TextField()# 상품 이름
    musinPrice = models.TextField()# 상품 가격
    

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
        
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)