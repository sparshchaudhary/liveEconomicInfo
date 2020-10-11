from django.shortcuts import render, HttpResponse, redirect
from Index.models import IndexNewsPost
from django.contrib import messages


# Create your views here.

def Index(request):
    allIndexNewsPost = IndexNewsPost.objects.all().order_by('-created_on')
    context = {'allIndexNewsPost':allIndexNewsPost}
    return render (request, 'Index/Index.html', context)

def about(request):
    return render(request, 'Index/About.html')

def contact(request):
    return render(request, 'Index/Contact.html')

def tnews(request, slug):
    trendpost = IndexNewsPost.objects.filter(slug=slug).first()
    context = {'trendpost':trendpost}
    return render(request, 'Index/tnews.html', context)





