from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
from shoppingmall.models import Goods, PhoneModel, Manufacturer, Comment

admin.site.register(Goods, MarkdownxModelAdmin)
admin.site.register(Comment)

class CategorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(PhoneModel, TagAdmin)
admin.site.register(Manufacturer, CategorAdmin)
