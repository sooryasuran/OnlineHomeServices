from django.urls import path

from OnlineHomeServiceApp import views

urlpatterns = [
    path('',views.homeview,name='homeview')
]