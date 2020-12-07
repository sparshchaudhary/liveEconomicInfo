from django.contrib import admin
from Stock.models import SwingTradePost, PreviousSwingTrade,StockCard, LongTermBet, StockMarketPageContact, StockMarketOpinionPost

# Register your models here.
admin.site.register(SwingTradePost)
admin.site.register(PreviousSwingTrade)
admin.site.register(StockCard)
admin.site.register(LongTermBet)
admin.site.register(StockMarketPageContact)

@admin.register(StockMarketOpinionPost)
class StockMarketOpinionPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)
