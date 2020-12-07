from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.Index, name='Index'),
    path('about', views.about, name='about'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('sow', views.sow, name='sow'),
    path('som', views.som, name='som'),
    path('hrhr', views.hrhr, name='hrhr'),
    path('privacy-policy', views.privacypolicy, name='privacypolicy'),
    path('terms-of-service', views.termsofservice, name='termsofservice'),
    path('new/<str:slug>', views.tnews, name='tnews'),
    path('trending/<str:Islug>', views.slidenews, name='slidenews'),
    path('global/<str:globalslug>', views.globalnews, name='globalnews'),
    path('govt/<str:testslug>', views.testingnewslug, name='testingnewslug'),
    path('stocknews/<str:stockmarketnewsslug>', views.lateststocknews, name='lateststocknews'),
    path('private/<str:privateslug>', views.indexprivatejob, name='indexprivatejob'),
    path('opinion/<str:opinionslug>', views.indexopinion, name='indexopinion'),

]

