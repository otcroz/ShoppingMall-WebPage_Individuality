from django.shortcuts import render
from shoppingmall.models import Goods

# Create your views here.
from django.shortcuts import render
from shoppingmall.models import Goods


def landing(request):
    recent_goods = Goods.objects.order_by('-pk')[:6]
    return render(request, 'home/landing.html',
                  {'recent_goods': recent_goods})   # html 파일과 연결

def introduce(request):
    return render(request, 'home/introduce.html')

def mypage(request):
    return render(request, 'home/mypage.html')