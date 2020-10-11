from django.contrib import admin
from Index.models import Contact, IndexValue, StockDetails, IndexPageStockContact, IndexJobPost, IndexNewsPost, IndexOtherPosts, StockOfTheWeek, StockOfTheMonth, HighRiskHighReturn, BookStore, NewsPic

# Register your models here.
admin.site.register(Contact)
admin.site.register(IndexPageStockContact)
admin.site.register(IndexValue)
admin.site.register(StockDetails)
admin.site.register(IndexOtherPosts)
admin.site.register(BookStore)
admin.site.register(NewsPic)

# admin.site.register(IndexJobPost)
@admin.register(IndexJobPost)
class IndexJobPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

# admin.site.register(IndexNewsPost)
@admin.register(IndexNewsPost)
class IndexNewsPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

# admin.site.register(StockOfTheWeek)
@admin.register(StockOfTheWeek)
class StockOfTheWeekAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


# admin.site.register(StockOfTheMonth)
@admin.register(StockOfTheMonth)
class StockOfTheMonthAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

# admin.site.register(HighRiskHighReturn)
@admin.register(HighRiskHighReturn)
class HighRiskHighReturnAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)




