#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index, name='index'),
]
