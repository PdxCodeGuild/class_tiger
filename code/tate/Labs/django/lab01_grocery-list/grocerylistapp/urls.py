from django.urls import path
from . import views

app_name = 'grocerylistapp'
urlpatterns = [
    path('', views.indexView, name='indexView'),
    path('addItem/', views.addItem, name= 'addItem'),
    path('<int:pk>/deleteItem', views.deleteItem, name= 'deleteItem'),
    path('<int:pk>/completeItem/', views.completeItem, name= 'completeItem')
]