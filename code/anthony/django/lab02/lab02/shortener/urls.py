from django.urls import path

from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:url_short>', views.new_url, name='new_url')

]