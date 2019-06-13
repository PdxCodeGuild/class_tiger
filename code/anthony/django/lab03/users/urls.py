from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('<str:username>/', views.ChirpList.as_view(), name='chirp_list'),
]
