from django.urls import path

from . import views

app_name = 'groceries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/completed', views.completed, name='completed'),
    path('add/', views.add, name='add'),
    path('<int:pk>/delete', views.delete, name='delete'),
    
]