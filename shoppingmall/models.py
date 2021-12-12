from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
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
    delivery_fee = models.CharField(max_length=15, blank=True)  # 배송비
    content = MarkdownxField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL, blank=True)  # 제조사(브랜드)
    PhoneModel = models.ManyToManyField(PhoneModel, blank=True)  # 폰 기종
    country = models.CharField(max_length=20) # 제조국

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)  # 사용자

    class Meta:
        verbose_name_plural = 'Goods'

    def __str__(self):  # 게시글 제목
        return f'[{self.manufacturer}] {self.name}'  # primary_key, 제목

    def get_absolute_url(self):
        return f'/goods/{self.pk}/'

    def get_content_markdown(self):  # content 내용을 markdowm으로 변경
        return markdown(self.content)

class Comment(models.Model): # 댓글 모델
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.goods.get_absolute_url()}#comment-{self.pk}/'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/389/0bb9b17cd7ab4167/svg/{{self.author.email}}/'




