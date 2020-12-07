from django.shortcuts import render, HttpResponse, redirect
from Gjob.models import BookPost, LatestGovJobPost, GjobPageContact
from django.contrib import messages

# Create your views here.

def gjob(request):
    allLatestGovJobPost = LatestGovJobPost.objects.all().order_by('-created_on')
    allBookPost = BookPost.objects.all()
    context = {'allBookPost':allBookPost, 'allLatestGovJobPost':allLatestGovJobPost}
    if request.method =='POST':
        useremail =request.POST['useremail']

        if len(useremail)<4 :
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            Gjobcontact = GjobPageContact(useremail=useremail)
            Gjobcontact.save()
            messages.success(request, "Great, Your message has been successfully sent. You will start getting recommendations now onwards.")
    return render(request, 'Gjob/GjobHome.html', context)
    
def gsearch(request):
    gquery =request.GET['gquery']
    if len(gquery)>50:
        allLatestGovJobPost = LatestGovJobPost.objects.none()
    else:
        allLatestGovJobPost = LatestGovJobPost.objects.filter(category__icontains=gquery)

    if allLatestGovJobPost.count()== 0:
        messages.warning(request, "No search result found. Please refine your query.")
    params = {'allLatestGovJobPost': allLatestGovJobPost, 'gquery':gquery}
    return render(request, 'Gjob/gsearch.html', params)
    
def LatestGjobPost(request,Gslug):
    Lgjobpost = LatestGovJobPost.objects.filter(Gslug=Gslug).first()
    allBookPost = BookPost.objects.all()
    Lgjobpost.views = Lgjobpost.views + 1
    Lgjobpost.save()
    context = {'Lgjobpost':Lgjobpost, 'allBookPost':allBookPost}
    if request.method =='POST':
        useremail =request.POST['useremail']

        if len(useremail)<4 :
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            Gjobcontact = GjobPageContact(useremail=useremail)
            Gjobcontact.save()
            messages.success(request, "Great, Your message has been successfully sent. You will start getting recommendations now onwards.")
    return render(request, 'Gjob/LatestGjobPost.html', context)


