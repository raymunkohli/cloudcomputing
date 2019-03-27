from django.urls import path
from django.views.decorators.csrf import csrf_exempt   

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
    path('loggedin', csrf_exempt(views.loggedin), name='loggedin'),
    path('addsong', views.addsong, name = "addsong")
]