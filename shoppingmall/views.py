from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView  # CBV 형식
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Goods, PhoneModel, Manufacturer
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
def new_comment(request, pk):
    if request.user.is_authenticated:
        goods = get_object_or_404(Goods, pk=pk)
        if request.method == 'POST' :
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.goods = goods
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(goods.get_absolute_url())
    else:
        raise PermissionDenied

class GoodsUpdate(LoginRequiredMixin, UpdateView):  # 모델명_form
    model = Goods
    fields = ['name', 'image', 'price', 'delivery_fee', 'content', 'manufacturer', 'PhoneModel', 'country']

    template_name = 'shoppingmall/goods_update_form.html'  # PostCreate와 기본 설정 이름이 동일하기에 따로 설정한다.

    def dispatch(self, request, *args, **kwargs): # get과 post(접근 방법)를 구분
        if request.user.is_authenticated  and request.user == self.get_object().author:
            return super(GoodsUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GoodsUpdate, self).get_context_data() # super가 가지고 있는 것을 상송
        if self.object.PhoneModel.exists():
            tags_str_list = list()
            for t in self.object.PhoneModel.all():
                tags_str_list.append(t.name)
            context['tag_str_default'] = '; '.join(tags_str_list)
        return context

    def form_valid(self, form):  # 태그 처리
        response = super(GoodsUpdate, self).form_valid(form)
        self.object.PhoneModel.clear()  # 기존의 태그 지움
        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip()
            tags_str = tags_str.replace(',', ';')
            tags_list = tags_str.split(';')
            for t in tags_list:
                t = t.strip()
                tag, is_tag_created = PhoneModel.objects.get_or_create(name=t)
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.PhoneModel.add(tag)
        return response

class GoodsCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Goods
    fields = ['name', 'image', 'price', 'delivery_fee', 'content', 'manufacturer', 'PhoneModel', 'country']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):  # 폼 처리
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user  # author 필드값을 부여
            response = super(GoodsCreate, self).form_valid(form)
            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()
                tags_str = tags_str.replace(',', ';')
                tags_list = tags_str.split(';')
                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = PhoneModel.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)
            return response
        else :
            return redirect('/goods/')

# 상품 목록
class GoodsList(ListView):
    model = Goods
    ordering = '-pk'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GoodsList, self).get_context_data()  # super가 가지고 있는 것을 상송
        context['manufacturers'] = Manufacturer.objects.all()
        return context

# 상품 상세
class GoodsDetail(DetailView):
    model = Goods

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GoodsDetail, self).get_context_data()  # super가 가지고 있는 것을 상송
        context['manufacturers'] = Manufacturer.objects.all()
        context['comment_form'] = CommentForm

        # context['comment_form'] = CommentForm
        return context

def category_page(request, slug):
    if slug == 'no_manufacturer': #수정
        manufacturer = '미분류'
        goods_list = Goods.objects.filter(manufacturer=None)
    else:
        manufacturer = Manufacturer.objects.get(slug=slug)
        goods_list = Goods.objects.filter(manufacturer=manufacturer)

    return render(request, 'shoppingmall/goods_list.html',
                  {
                      'goods_list': goods_list,
                      'manufacturers': Manufacturer.objects.all(),
                      'manufacturer': manufacturer
                  }
                  )
def tag_page(request, slug):
    phonemodel = PhoneModel.objects.get(slug=slug)
    goods_list = phonemodel.post_set.all()  # Post.objects.filter(tags=tag)

    return render(request, 'goods/goods_list.html',
                  {
                      'goods_list': goods_list,
                      'phonemodels': PhoneModel.objects.all(),
                      'no_phonemodel_goods_count': Goods.objects.filter(PhoneModel=None).count(),
                      'phonemodel': phonemodel
                  }
                  )