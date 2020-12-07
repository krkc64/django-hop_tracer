from django.urls import re_path
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='default'),
    re_path(r'map$', views.response, name='response'),
]