from django.shortcuts import render, HttpResponse, redirect
from Stock.models import SwingTradePost, PreviousSwingTrade, StockCard, LongTermBet
from django.contrib import messages


# Create your views here.

def page(request):
    allSwingTradePost = SwingTradePost.objects.all().order_by('-created_on')
    allStockCard = StockCard.objects.all().order_by('-created_on')
    allLongTermBet = LongTermBet.objects.all().order_by('-created_on')
    context = {'allSwingTradePost':allSwingTradePost, 'allStockCard':allStockCard, 'allLongTermBet':allLongTermBet}
    return render(request, 'Stock/StockHome.html', context)
    return HttpResponse('THIS IS Stock app')


def lasttrade(request):
    allPreviousSwingTrade = PreviousSwingTrade.objects.all().order_by('-created_on')
    context = {'allPreviousSwingTrade':allPreviousSwingTrade}
    return render(request, 'Stock/lasttrade.html', context)

def ssearch(request):
    squery =request.GET['squery']
    if len(squery)>50:
        allSwingTradePost = SwingTradePost.objects.none()

    else:
        allSwingTradePost = SwingTradePost.objects.filter(stockname__icontains=squery)

    if allSwingTradePost.count()== 0:
        messages.warning(request, "No search result found. Please refine your query.")
    params = {'allSwingTradePost': allSwingTradePost, 'squery':squery}
    return render(request, 'Stock/ssearch.html', params)

def StockPost(request, slug):
    swingtradepost = SwingTradePost.objects.filter(slug=slug).first()
    context = {'swingtradepost':swingtradepost}
    return render(request, 'Stock/StockPost.html', context)
