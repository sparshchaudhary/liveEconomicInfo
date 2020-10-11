from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<str:slug>', views.tnews, name='tnews'),
]
