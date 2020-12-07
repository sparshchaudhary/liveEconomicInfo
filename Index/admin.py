from django.contrib import admin
from Index.models import Contact, StockDetails, IndexPageStockContact, IndexJobPost, IndexNewsPost, StockOfTheWeek, StockOfTheMonth, HighRiskHighReturn, BookStore, NewsPic, IndexGlobalNewsPost, IndexPrivateJobPost, StockMarketLatestNewsCard, IndexStockMarketDailyUpdatedNews, IndexSlideNewsPost, IndicesValueIndexPage, IndexOpinion

# Register your models here.
admin.site.register(Contact)
admin.site.register(IndexPageStockContact)
admin.site.register(IndicesValueIndexPage)
admin.site.register(StockDetails)
admin.site.register(BookStore)
admin.site.register(NewsPic)
admin.site.register(StockMarketLatestNewsCard)

@admin.register(IndexJobPost)
class IndexJobPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(IndexNewsPost)
class IndexNewsPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(IndexSlideNewsPost)
class IndexSlideNewsPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(IndexStockMarketDailyUpdatedNews)
class IndexStockMarketDailyUpdatedNewsAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(IndexPrivateJobPost)
class IndexPrivateJobPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(IndexGlobalNewsPost)
class IndexGlobalNewsPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(IndexOpinion)
class IndexOpinionAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(StockOfTheWeek)
class StockOfTheWeekAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(StockOfTheMonth)
class StockOfTheMonthAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

@admin.register(HighRiskHighReturn)
class HighRiskHighReturnAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


