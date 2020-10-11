from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('finance', views.news, name='news'),
    path('<str:slug>', views.FinanceNewsPostPage, name='FinanceNewsPostPage')
]

