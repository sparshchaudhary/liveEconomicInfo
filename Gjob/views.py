from django.shortcuts import render, HttpResponse, redirect
from Gjob.models import GovJobPost, BookPost
from django.contrib import messages

# Create your views here.

def gjob(request):
    allGovJobPost = GovJobPost.objects.all().order_by('-created_on')
    allBookPost = BookPost.objects.all()
    context = {'allGovJobPost':allGovJobPost, 'allBookPost':allBookPost}
    return render(request, 'Gjob/GjobHome.html', context)
    # return HttpResponse('THIS IS Government Job  app')

def gsearch(request):
    gquery =request.GET['gquery']
    if len(gquery)>50:
        allGovJobPost = GovJobPost.objects.none()
    else:
        allGovJobPost = GovJobPost.objects.filter(category__icontains=gquery)
        # allFinanceNewsPostContent = FinanceNewsPost.objects.filter(content__icontains=query)
        # allFinanceNewsPost = allFinanceNewsPostTitle.union(allFinanceNewsPostContent)

    if allGovJobPost.count()== 0:
        messages.warning(request, "No search result found. Please refine your query.")
    params = {'allGovJobPost': allGovJobPost, 'gquery':gquery}
    return render(request, 'Gjob/gsearch.html', params)
    
def GjobPost(request,slug):
    gjobpost = GovJobPost.objects.filter(slug=slug).first()
    allBookPost = BookPost.objects.all()
    gjobpost.views = gjobpost.views + 1
    gjobpost.save()
    context = {'gjobpost':gjobpost, 'allBookPost':allBookPost}
    return render(request, 'Gjob/GjobPost.html', context)
