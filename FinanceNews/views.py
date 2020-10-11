from django.shortcuts import render, HttpResponse, redirect
from FinanceNews.models import FinanceNewsPost, SideNewsPics,HeaderNewsPics


# Create your views here.
def news(request):
    allFinanceNewsPost = FinanceNewsPost.objects.all().order_by('-created_on')
    allSideNewsPics = SideNewsPics.objects.all()
    allHeaderNewsPics = HeaderNewsPics.objects.all()
    context = {'allFinanceNewsPost':allFinanceNewsPost, 'allSideNewsPics':allSideNewsPics, 'allHeaderNewsPics':allHeaderNewsPics}
    return render(request, 'FinanceNews/FinanceNewsHome.html', context)
    # return HttpResponse('THIS IS News app')


def FinanceNewsPostPage(request, slug):
    fnewspost = FinanceNewsPost.objects.filter(slug=slug).first()
    fnewspost.views = fnewspost.views + 1
    fnewspost.save()
    context = {'fnewspost':fnewspost}
    return render(request, 'FinanceNews/FinanceNewsPostPage.html', context)

