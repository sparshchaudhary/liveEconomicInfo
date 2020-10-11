from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('market', views.page, name='page'),
    path('lasttrade', views.lasttrade, name='lasttrade'),
    path('ssearch', views.ssearch, name='ssearch'),
    path('<str:slug>', views.StockPost, name='StockPost')
]


