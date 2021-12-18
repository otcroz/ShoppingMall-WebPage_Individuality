from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
from shoppingmall.models import Goods, PhoneModel, Manufacturer, Comment, CaseType

admin.site.register(Goods, MarkdownxModelAdmin)
admin.site.register(Comment)


class CategorAdmin(admin.ModelAdmin): # 제조사
    prepopulated_fields = {'slug': ('name',)}

class CategorAdmin2(admin.ModelAdmin): # 케이스 종류
    prepopulated_fields = {'slug': ('type',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(PhoneModel, TagAdmin)
admin.site.register(Manufacturer, CategorAdmin)
admin.site.register(CaseType, CategorAdmin2)
