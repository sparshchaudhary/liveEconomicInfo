from django.contrib import admin
from FinanceNews.models import FinanceNewsPost, SideNewsPics, HeaderNewsPics

# Register your models here.
# admin.site.register(FinanceNewsPost)

admin.site.register(SideNewsPics)
admin.site.register(HeaderNewsPics)

@admin.register(FinanceNewsPost)
class FinanceNewsPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

