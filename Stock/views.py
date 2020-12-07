from django.shortcuts import render, HttpResponse, redirect
from Stock.models import SwingTradePost, PreviousSwingTrade, StockCard, LongTermBet, StockMarketPageContact, StockMarketOpinionPost
from Index.models import StockMarketLatestNewsCard, IndicesValueIndexPage, StockDetails
from django.contrib import messages

# Create your views here.

def page(request):
    allSwingTradePost = SwingTradePost.objects.all().order_by('-created_on')
    allStockMarketOpinionPost = StockMarketOpinionPost.objects.all().order_by('-created_on')
    allStockCard = StockCard.objects.all().order_by('-created_on')
    allLongTermBet = LongTermBet.objects.all().order_by('-created_on')
    allStockMarketLatestNewsCard = StockMarketLatestNewsCard.objects.all()
    allIndicesValueIndexPage = IndicesValueIndexPage.objects.all().order_by('-created_on')
    allStockDetails = StockDetails.objects.all().order_by('-created_on')
    context = {'allSwingTradePost':allSwingTradePost, 'allStockCard':allStockCard, 'allLongTermBet':allLongTermBet, 'allStockMarketLatestNewsCard':allStockMarketLatestNewsCard, 'allIndicesValueIndexPage':allIndicesValueIndexPage, 'allStockDetails':allStockDetails, 'allStockMarketOpinionPost':allStockMarketOpinionPost}
    if request.method =='POST':
        useremail =request.POST['useremail']

        if len(useremail)<4 :
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            stockmarketcontact = StockMarketPageContact(useremail=useremail)
            stockmarketcontact.save()
            messages.success(request, "Great, Your message has been successfully sent. You will start getting recommendations now onwards.")
    return render(request, 'Stock/StockHome.html', context)

def lasttrade(request):
    allPreviousSwingTrade = PreviousSwingTrade.objects.all().order_by('-created_on')
    allStockMarketLatestNewsCard = StockMarketLatestNewsCard.objects.all()
    allIndicesValueIndexPage = IndicesValueIndexPage.objects.all().order_by('-created_on')
    context = {'allPreviousSwingTrade':allPreviousSwingTrade, 'allStockMarketLatestNewsCard':allStockMarketLatestNewsCard, 'allIndicesValueIndexPage':allIndicesValueIndexPage}
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
    allStockMarketLatestNewsCard = StockMarketLatestNewsCard.objects.all()
    context = {'swingtradepost':swingtradepost, 'allStockMarketLatestNewsCard':allStockMarketLatestNewsCard}
    if request.method =='POST':
        useremail =request.POST['useremail']

        if len(useremail)<4 :
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            stockmarketcontact = StockMarketPageContact(useremail=useremail)
            stockmarketcontact.save()
            messages.success(request, "Great, Your message has been successfully sent. You will start getting recommendations now onwards.")
    return render(request, 'Stock/StockPost.html', context)

def StockMarketOpinion(request, stockopinionslug):
    SMopinionpost = StockMarketOpinionPost.objects.filter(stockopinionslug=stockopinionslug).first()
    allStockMarketLatestNewsCard = StockMarketLatestNewsCard.objects.all()
    context = {'SMopinionpost':SMopinionpost, 'allStockMarketLatestNewsCard':allStockMarketLatestNewsCard}
    if request.method =='POST':
        useremail =request.POST['useremail']

        if len(useremail)<4 :
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            stockmarketcontact = StockMarketPageContact(useremail=useremail)
            stockmarketcontact.save()
            messages.success(request, "Great, Your message has been successfully sent. You will start getting recommendations now onwards.")
    return render(request, 'Stock/stockmarketopinion.html', context)


