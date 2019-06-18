from django.urls import path
from . import views

app_name = 'chirp'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('feed', views.ChirpListView.as_view(), name='feed'),
    path('chirp/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('chirp/new/', views.ChirpCreateView.as_view(), name='new'),
    path('chirp/<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete'),

]