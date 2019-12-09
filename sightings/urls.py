from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import re_path


urlpatterns = [
    path('',views.index, name = 'index'),
    re_path(r'(\w+-[A-Za-z]{2}-\d{4}-\d{2})/', views.edit, name='edit'),
    path('add/',views.add, name = 'add'),
    path('stats/',views.stats, name = 'stats'),
]
