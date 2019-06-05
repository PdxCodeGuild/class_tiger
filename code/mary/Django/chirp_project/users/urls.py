from django.urls import path
from . import views

app_name='users'

urlpatterns=[
    path('', views.UsernameListView.as_view(), name='username_list'),
    path('signup/', views.CreateLogInView.as_view(), name='create_log'),
    path('<str:username>/', views.PostList.as_view(), name='post_list'),
]