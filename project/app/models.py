from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class lotteData(models.Model):
    search_lotte = models.TextField()#검색어 필드
    lotteImage = models.ImageField(upload_to='images/', blank=True)# 상품 이미지
    lotteUrl = models.TextField()# 상품 이미지 URL
    lotteName = models.TextField()# 상품 이름
    lottePrice = models.TextField()# 상품 가격
    

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
        
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

#장바구니 구현
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product  = models.ForeignKey(lotteData, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    # 수량은 -1 과 같은 수량이 없기 때문에 아래의 필드로 선언하여 최소값을 1 로 설정
    quantity = models.PositiveSmallIntegerField(null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '장바구니'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-pk']

    # def sub_total(self):
    # 	# 템플릿에서 사용하는 변수로 장바구니에 담긴 각 상품의 합계
    #     return self.lotte.price * self.quantity

    def __str__(self):
        return self.product.lotteName