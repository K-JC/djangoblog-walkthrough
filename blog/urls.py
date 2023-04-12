from . import views
from django.urls import path

urls = [
    path('', views.PostList.as_view(), name='home')
]