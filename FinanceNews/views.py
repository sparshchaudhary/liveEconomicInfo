from django.shortcuts import render, HttpResponse, redirect
from FinanceNews.models import SideNewsPics, HeaderNewsPics, LatestFinancenewspost
from Index.models import IndicesValueIndexPage


# Create your views here.
def news(request):
    allLatestFinancenewspost = LatestFinancenewspost.objects.all().order_by('-created_on')
    allSideNewsPics = SideNewsPics.objects.all()
    allHeaderNewsPics = HeaderNewsPics.objects.all()
    allIndicesValueIndexPage = IndicesValueIndexPage.objects.all().order_by('-created_on')
    context = {'allSideNewsPics':allSideNewsPics, 'allHeaderNewsPics':allHeaderNewsPics, 'allLatestFinancenewspost':allLatestFinancenewspost, 'allIndicesValueIndexPage':allIndicesValueIndexPage}
    return render(request, 'FinanceNews/FinanceNewsHome.html', context)


def FinancenewspostPage(request, Fslug):
    Fnewspost = LatestFinancenewspost.objects.filter(Fslug=Fslug).first()
    Fnewspost.views = Fnewspost.views + 1
    Fnewspost.save()
    allSideNewsPics = SideNewsPics.objects.all()
    allIndicesValueIndexPage = IndicesValueIndexPage.objects.all().order_by('-created_on')
    context = {'Fnewspost':Fnewspost, 'allSideNewsPics':allSideNewsPics, 'allIndicesValueIndexPage':allIndicesValueIndexPage}
    return render(request, 'FinanceNews/FinancenewspostPage.html', context)

