from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.
class Manufacturer(models.Model): # 기종 / 태그
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/goods/manufacturer/{self.slug}'

    class Meta:  # 모델의 이름 수정
        verbose_name_plural = 'Manufacturers'

class PhoneModel(models.Model): # 제조사(브랜드) / 카테고리
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/goods/phonemodel/{self.slug}'

class Goods(models.Model): # 상품
    name = models.CharField(max_length=50)  # 이름
    image = models.ImageField(upload_to='blog/images/', blank=True) # 이미지
    price = models.CharField(max_length=15)  # 가격
    content = models.TextField();

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL, blank=True)  # 제조사(브랜드)
    PhoneModel = models.ManyToManyField(PhoneModel, blank=True)  # 폰 기종
    country = models.CharField(max_length=20) # 제조국

    date = models.DateTimeField()  # 제조연월

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)  # 사용자

    def __str__(self):  # 게시글 제목
        return f'[{self.manufacturer}] {self.name}'  # primary_key, 제목

    def get_absolute_url(self):
        return f'/goods/{self.pk}/'

    class Meta:
        verbose_name_plural = 'Goods'



