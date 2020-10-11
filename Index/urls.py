from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('sow', views.sow, name='sow'),
    path('som', views.som, name='som'),
    path('hrhr', views.hrhr, name='hrhr'),
    path('<str:slug>', views.tnews, name='tnews'),
    path('govt/<str:testslug>', views.testingnewslug, name='testingnewslug'),

]
