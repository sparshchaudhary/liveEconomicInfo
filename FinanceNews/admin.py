from django.contrib import admin
from FinanceNews.models import SideNewsPics, HeaderNewsPics, LatestFinancenewspost

# Register your models here.
# admin.site.register(FinanceNewsPost)

admin.site.register(SideNewsPics)
admin.site.register(HeaderNewsPics)

@admin.register(LatestFinancenewspost)
class LatestFinancenewspostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

