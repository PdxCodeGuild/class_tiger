from django.urls import path

from . import views

app_name = 'chirps'

urlpatterns = [
    path('', views.ChirpListView.as_view(), name='home'),
    path('chirp/detail/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('chirp/delete/<int:pk>/', views.ChirpDeleteView.as_view(), name='delete'),
    path('chirp/create', views.ChirpCreateView.as_view(), name='create'),
    path('chirp/comment/<int:pk>/', views.post_comment, name='comment'),
    path('chirp/like/<int:pk>/', views.add_like, name='like'),
]
