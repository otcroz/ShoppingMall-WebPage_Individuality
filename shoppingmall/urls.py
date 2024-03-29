from django.urls import path
from . import views

urlpatterns = [
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('search/<str:q>/', views.GoodsSearch.as_view()),
    path('update_post/<int:pk>/', views.GoodsUpdate.as_view()),
    path('create_post/', views.GoodsCreate.as_view()),
    path('phonemodel/<str:slug>', views.tag_page),
    path('manufacturer/<str:slug>', views.category_page),
    path('casetype/<str:slug>', views.casetype_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/', views.GoodsDetail.as_view()),
    path('', views.GoodsList.as_view()),
]