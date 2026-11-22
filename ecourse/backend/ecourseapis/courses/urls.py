from django.contrib import admin
from courses import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = 'home')
]