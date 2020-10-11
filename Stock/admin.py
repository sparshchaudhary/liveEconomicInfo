from django.contrib import admin
from Stock.models import SwingTradePost, PreviousSwingTrade,StockCard, LongTermBet

# Register your models here.
admin.site.register(SwingTradePost)
admin.site.register(PreviousSwingTrade)
admin.site.register(StockCard)
admin.site.register(LongTermBet)
