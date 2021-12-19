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
    manufacturers = Manufacturer.objects.all()
    casetypes = CaseType.objects.all()

    # 개수 배열
    manu_count = []
    for manu in manufacturers:
        manu_count.append(Goods.objects.filter(manufacturer=manu).count())

    case_count = []
    for case in casetypes:
        case_count.append(Goods.objects.filter(case_type=case).count())


    return render(request, 'home/introduce.html',
                  {
                    'manu_count': manu_count,
                    'case_count': case_count,
                    'manufacturers': Manufacturer.objects.all(),
                      'casetypes' : CaseType.objects.all(),

                  }
                  )

def mypage(request):
    return render(request, 'home/mypage.html')






