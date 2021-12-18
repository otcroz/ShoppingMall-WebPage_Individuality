from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('introduce/', views.introduce),
    path('mypage/', views.mypage),

]
