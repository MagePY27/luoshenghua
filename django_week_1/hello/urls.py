#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index, name='index'),
]
