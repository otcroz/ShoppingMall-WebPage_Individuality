from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView  # CBV 형식
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Goods, PhoneModel, Manufacturer
#from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

# 상품 목록
class GoodsList(ListView):
    model = Goods
    ordering = '-pk'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GoodsList, self).get_context_data()
        context['manufacturers'] = Manufacturer.objects.all()
        context['no_manufacturer_goods_count'] = Goods.objects.filter(manufacturer=None).count()
        return context

# 상품 상세
class GoodsDetail(DetailView):
    model = Goods

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GoodsDetail, self).get_context_data()  # super가 가지고 있는 것을 상송
        context['manufacturers'] = Manufacturer.objects.all()
        context['no_manufacturer_goods_count'] = Goods.objects.filter(manufacturer=None).count()
        # context['comment_form'] = CommentForm
        return context

def category_page(request, slug):
    if slug == 'no_manufacturer':
        manufacturer = '미분류'
        goods_list = Goods.objects.filter(manufacturer=None)
    else:
        manufacturer = Manufacturer.objects.get(slug=slug)
        goods_list = Goods.objects.filter(manufacturer=manufacturer)

    return render(request, 'shoppingmall/goods_list.html',
                  {
                      'goods_list': goods_list,
                      'manufacturers': Manufacturer.objects.all(),
                      'no_manufacturer_goods_count': Goods.objects.filter(manufacturer=None).count(),
                      'manufacturer': manufacturer
                  }
                  )
def tag_page(request, slug):
    tag = PhoneModel.objects.get(slug=slug)
    goods_list = tag.post_set.all()  # Post.objects.filter(tags=tag)

    return render(request, 'goods/goods_list.html',
                  {
                      'goods_list': goods_list,
                      'manufacturers': PhoneModel.objects.all(),
                      'no_manufacturer_goods_count': Goods.objects.filter(manufacturer=None).count(),
                      'tag': tag
                  }
                  )