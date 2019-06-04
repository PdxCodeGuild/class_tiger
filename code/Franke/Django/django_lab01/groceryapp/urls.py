from django.urls import path
from . import views

# set urls for each view in here
# functional way
app_name = 'groceryapp'
urlpatterns = [
    path('',views.index, name ='index'),
    path('done/<int:pk>/',views.done, name='done'),
    path('delete/<int:pk>/',views.delete, name='delete'),
]