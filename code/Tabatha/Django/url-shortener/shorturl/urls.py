from django.urls import path
from . import views

app_name = "shorturl"
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('<str:short>/', views.link, name='link'),
    path('show/<str:short>/', views.show_short, name='shorty')
]