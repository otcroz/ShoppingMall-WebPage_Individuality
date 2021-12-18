from django.shortcuts import render
from shoppingmall.models import Goods

# Create your views here.
from django.shortcuts import render
from shoppingmall.models import Goods, Manufacturer, CaseType


def landing(request):
    recent_goods = Goods.objects.order_by('-pk')[:6]
    return render(request, 'home/landing.html',
                  {'recent_goods': recent_goods})   # html 파일과 연결

def introduce(request):
    # 케이스 종류에 대한 차트
    cnt_hard = CaseType.objects.get(type="Hard Case")
    cnt_jelly = CaseType.objects.get(type="Jelly Case")
    cnt_card = CaseType.objects.get(type="Card Case")

    hard_case = Goods.objects.filter(case_type=cnt_hard).count()
    jelly_case = Goods.objects.filter(case_type=cnt_jelly).count()
    card_case = Goods.objects.filter(case_type=cnt_card).count()

    case_list_chart = [hard_case, jelly_case, card_case]

    # 제조사에 대한 차트
    cnt_earpearp = Manufacturer.objects.get(name="Earpearp")
    cnt_168cm = Manufacturer.objects.get(name="168cm")
    cnt_thenine = Manufacturer.objects.get(name="The Nine Mall")

    brand_earpearp = Goods.objects.filter(manufacturer=cnt_earpearp).count()
    brand_168cm = Goods.objects.filter(manufacturer=cnt_168cm).count()
    brand_theninemall = Goods.objects.filter(manufacturer=cnt_thenine).count()
    
    manufacturer_list_chart = [brand_earpearp, brand_168cm, brand_theninemall]
    return render(request, 'home/introduce.html',
                  {
                    'case_list_chart': case_list_chart,
                    'manufacturer_list_chart' : manufacturer_list_chart,
                  }
                  )

def mypage(request):
    return render(request, 'home/mypage.html')






