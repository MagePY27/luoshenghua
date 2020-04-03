#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

from django.urls import path
from hello.views import HelloIndex
from django.urls import re_path

urlpatterns = [
    path('', HelloIndex.index, name='index'),

    # 位置匹配
    # re_path("([0-9]{4})/([0-9]{2})/", HelloIndex.index, name="HelloIndex"),

    # 关键字匹配(最优雅) (?<参数名>参数类型)
    # re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/", HelloIndex.index2, name="HelloIndex2"),
]
