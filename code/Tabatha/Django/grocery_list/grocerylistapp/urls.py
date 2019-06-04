from django.urls import path
from . import views

app_name = "grocerylistapp"
urlpatterns = [
    path('', views.groceries, name='list'),
    path('<int:pk>/complete/', views.complete, name='complete'),
    path('add/', views.add_item, name='add'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    
]