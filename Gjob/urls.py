from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('latest', views.gjob, name='gjob'),
    path('gsearch', views.gsearch, name='gsearch'),
    path('recent/<str:Gslug>', views.LatestGjobPost, name='LatestGjobPost'),
]

