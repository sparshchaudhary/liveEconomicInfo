from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('finance', views.news, name='news'),
    path('latest/<str:Fslug>', views.FinancenewspostPage, name='FinancenewspostPage'),
]

