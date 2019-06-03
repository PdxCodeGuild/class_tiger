from django.urls import path
from . import views

app_name = 'urlshortenerapp' # for namespacing
urlpatterns = [
    path('', views.indexView, name='indexView'),
    path('addURL/', views.addURL, name= 'addURL'),
    path('info/', views.infoView, name= 'infoView'),

    path('<str:short_URL>/viewShortcode/', views.viewShortcode, name= 'viewShortcode')

]