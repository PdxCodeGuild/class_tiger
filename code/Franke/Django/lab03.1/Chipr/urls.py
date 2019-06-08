"""Chipr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from chirps.views import feed
from chirprprofile.views import frontpage, signout, profile, follows, followers, follow, stopfollow 

urlpatterns = [
  path('', frontpage, name='frontpage'),
  path('feed/', feed, name='feed'), 
  path('signout/', signout, name='signout'),
  path('<str:username>/follows/', follows, name='follows'),
  path('<str:username>/followers/', followers, name='followers'),  
  path('<str:username>/follow/', follow, name='follow'), 
  path('<str:username>/stopfollow/', stopfollow, name='stopfollow'),
  path('<str:username>/', profile, name='profile'),
]