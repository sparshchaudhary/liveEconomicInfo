from django.shortcuts import render, HttpResponse, redirect
from Index.models import Contact, IndicesValueIndexPage, StockDetails, IndexPageStockContact, IndexJobPost, IndexNewsPost, StockOfTheWeek, StockOfTheMonth, HighRiskHighReturn, BookStore, NewsPic, IndexGlobalNewsPost, IndexPrivateJobPost, StockMarketLatestNewsCard, IndexStockMarketDailyUpdatedNews, IndexSlideNewsPost, IndexOpinion
from FinanceNews.models import SideNewsPics
from Gjob.models import BookPost
from django.contrib import messages

# Create your views here.

def handler404(request, *args, **argv):
    return render(request, '404.html')

def Index(request):
    allIndicesValueIndexPage = IndicesValueIndexPage.objects.all().order_by('-created_on')
    allStockDetails = StockDetails.objects.all().order_by('-created_on')
    allIndexJobPost = IndexJobPost.objects.all().order_by('-created_on')
    allIndexStockMarketDailyUpdatedNews = IndexStockMarketDailyUpdatedNews.objects.all().order_by('-created_on')
    allIndexPrivateJobPost = IndexPrivateJobPost.objects.all().order_by('-created_on')
    allIndexNewsPost = IndexNewsPost.objects.all().order_by('-created_on')
    allIndexSlideNewsPost = IndexSlideNewsPost.objects.all().order_by('-created_on')
    allIndexGlobalNewsPost = IndexGlobalNewsPost.objects.all().order_by('-created_on')
    allIndexOpinion = IndexOpinion.objects.all().order_by('-created_on')
    allBookStore = BookStore.objects.all().order_by('-created_on')
    allNewsPic = NewsPic.objects.all()
    allStockMarketLatestNewsCard = StockMarketLatestNewsCard.objects.all()
    context = {'allIndicesValueIndexPage':allIndicesValueIndexPage, 'allStockDetails':allStockDetails, 'allIndexJobPost':allIndexJobPost, 'allIndexNewsPost':allIndexNewsPost, 'allBookStore':allBookStore, 'allNewsPic':allNewsPic, 'allIndexPrivateJobPost':allIndexPrivateJobPost, 'allIndexGlobalNewsPost':allIndexGlobalNewsPost, 'allStockMarketLatestNewsCard':allStockMarketLatestNewsCard, 'allIndexStockMarketDailyUpdatedNews':allIndexStockMarketDailyUpdatedNews, 'allIndexSlideNewsPost':allIndexSlideNewsPost, 'allIndexOpinion':allIndexOpinion}
    if request.method =='POST':
        username = request.POST['username']
        useremail =request.POST['useremail']
        userphone =request.POST['userphone']

        if len(username)<2 or len(useremail)<4 or len(userphone)<10 :
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            stockcontact = IndexPageStockContact(username=username, useremail=useremail, userphone=userphone)
            stockcontact.save()
            messages.success(request, "Great, Your message has been successfully sent. You will start getting recommendations now onwards.")

    return render (request, 'Index/Index.html', context)

def about(request):
    return render(request, 'Index/About.html')

def sitemap(request):
    return render(request, 'Index/sitemap.xml')

def contact(request):
    if request.method=='POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<2:
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Thank you , Your message has been successfully sent.")
    return render(request, 'Index/Contact.html')

def search(request):
    query =request.GET['query']
    if len(query)>50:
        allIndexNewsPost = IndexNewsPost.objects.none()
    else:
        allIndexNewsPost = IndexNewsPost.objects.filter(title__icontains=query)
        #allFinanceNewsPostContent = FinanceNewsPost.objects.filter(content__icontains=query)
        #allFinanceNewsPost = allFinanceNewsPostTitle.union(allFinanceNewsPostContent)

    if allIndexNewsPost.count()== 0:
        messages.warning(request, "No search result found. Please refine your query.")
    params = {'allIndexNewsPost': allIndexNewsPost, 'query':query}
    return render(request, 'Index/search.html', params)

def sow(request):
    allStockOfTheWeek = StockOfTheWeek.objects.all().order_by('-created_on')
    allIndicesValueIndexPage = IndicesValueIndexPage.objects.all().order_by('-created_on')
    context = {'allStockOfTheWeek':allStockOfTheWeek,'allIndicesValueIndexPage':allIndicesValueIndexPage}
    return render(request, 'Index/sow.html', context)

def som(request):
    allStockOfTheMonth = StockOfTheMonth.objects.all().order_by('-created_on')
    context = {'allStockOfTheMonth':allStockOfTheMonth}
    return render(request, 'Index/som.html', context)

def hrhr(request):
    allHighRiskHighReturn = HighRiskHighReturn.objects.all().order_by('-created_on')
    context = {'allHighRiskHighReturn':allHighRiskHighReturn}
    return render(request, 'Index/hrhr.html', context)

def tnews(request, slug):
    trendpost = IndexNewsPost.objects.filter(slug=slug).first()
    allSideNewsPics = SideNewsPics.objects.all()
    context = {'trendpost':trendpost,'allSideNewsPics':allSideNewsPics}
    return render(request, 'Index/tnews.html', context)

def slidenews(request, Islug):
    slidetrendpost = IndexSlideNewsPost.objects.filter(Islug=Islug).first()
    allSideNewsPics = SideNewsPics.objects.all()
    context = {'slidetrendpost':slidetrendpost,'allSideNewsPics':allSideNewsPics}
    return render(request, 'Index/slidenews.html', context)

def globalnews(request, globalslug):
    gtrendpost = IndexGlobalNewsPost.objects.filter(globalslug=globalslug).first()
    context = {'gtrendpost':gtrendpost}
    return render(request, 'Index/globalnews.html', context)

def indexopinion(request, opinionslug):
    indexopinionpost = IndexOpinion.objects.filter(opinionslug=opinionslug).first()
    context = {'indexopinionpost':indexopinionpost}
    return render(request, 'Index/opinion.html', context)

def testingnewslug(request, testslug):
    trendgpost = IndexJobPost.objects.filter(testslug=testslug).first()
    allSideNewsPics = SideNewsPics.objects.all()
    allBookPost = BookPost.objects.all()
    context = {'trendgpost':trendgpost, 'allSideNewsPics':allSideNewsPics, 'allBookPost':allBookPost}
    return render(request, 'Index/indexjobslug.html', context) #context

def lateststocknews(request, stockmarketnewsslug):
    lstockmarketnews = IndexStockMarketDailyUpdatedNews.objects.filter(stockmarketnewsslug=stockmarketnewsslug).first()
    context = {'lstockmarketnews':lstockmarketnews}
    return render(request, 'Index/indexstockmarketnews.html', context)

def indexprivatejob(request, privateslug):
    privatetrendgpost = IndexPrivateJobPost.objects.filter(privateslug=privateslug).first()
    context = {'privatetrendgpost':privatetrendgpost}
    return render(request, 'Index/indexprivatejob.html', context)

def privacypolicy(request):
    return render(request, 'Index/privacy.html')

def termsofservice(request):
    return render(request, 'Index/termsofservice.html')

