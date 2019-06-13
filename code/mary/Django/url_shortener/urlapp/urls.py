from django.urls import path

from . import views

app_name='urlapp'

urlpatterns=[
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('<short_url>/', views.shorten, name='shorten'),
    ]