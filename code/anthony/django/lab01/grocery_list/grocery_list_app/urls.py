from django.urls import path

from . import views

app_name = 'grocery_list_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:pk>/', views.complete, name="complete"),
    path('remove/<int:pk>/', views.remove, name='remove'),

]
