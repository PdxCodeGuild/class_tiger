from django.urls import path
from . import views

app_name = 'chirps'

urlpatterns = [
    path('',views.HomeView.as_view(), name='index'),
    path('chirp/<int:pk>/',views.ChirpDetail.as_view(), name='detail'),
    path('chirp/new/',views.ChirpCreate.as_view(), name='new'),
    path('chirp/<int:pk>/edit/',views.ChirpEdit.as_view(), name='edit'),
    path('chirp/<int:pk>/delete/',views.ChirpDelete.as_view(), name='delete'),

]
