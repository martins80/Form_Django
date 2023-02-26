from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render

app_name = 'forms'
urlpatterns = [
    path('', views.index, name='mi_form'),
    
]