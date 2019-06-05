# from django.conf.urls import include, url
# from django.conf.urls.defaults import include, patterns, url
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'url_shortener'

urlpatterns = [
     url(r'^$', views.index, name='home'),
    # for our home/index page
 
    url(r'^(?P<short_id>\w{6})$', views.redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL
 
    url(r'^makeshort/$', views.shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL
    # ... your url patterns
]

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('redirectoriginal/<int:pk>/', views.redirect_original, name='redirectoriginal'),
#     path('shortenurl/<int:pk>/', views.shorten_url, name='shortenurl'),

# ]