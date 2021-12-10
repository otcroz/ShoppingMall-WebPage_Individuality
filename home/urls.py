from django.urls import path
from . import views

urlpatterns = [ # 서버IP/
    path('', views.landing),  # 서버IP/
    path('introduce/', views.introduce) # 서버IP/about_me # 회사 소개
]
