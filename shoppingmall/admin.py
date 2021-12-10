from django.contrib import admin

# Register your models here.
from shoppingmall.models import Goods, PhoneModel, Manufacturer

admin.site.register(Goods)

class CategorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Category 이름을 입력하면 자동으로 slug를 입력

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(PhoneModel, CategorAdmin)
admin.site.register(Manufacturer,TagAdmin)