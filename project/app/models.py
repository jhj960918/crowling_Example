from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="writer",default="")
    imagesearch = models.ImageField(blank=True)
    musinsaImage = models.ImageField(blank=True)
    
    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
        
    grade = models.CharField(max_length=20)
    major = models.CharField(max_length=20)

class musinsaData(models.Model):
    search_musinsa = models.TextField()#검색어 필드
    musinsaImage = models.ImageField(upload_to='images/', blank=True)# 상품 이미지
    musinsaUrl = models.TextField()# 상품 이미지 URL
    

