#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from hello.models import User

def index(request):
    # return HttpResponse('<p>This is hello index.</p>')
    users = User.objects.all()
    return render(request, "hello.html", {'users':users})


# def index(request):
#     print(request.scheme)  # http
#     print(request.method)  # GET POST DELETE PUT...
#     print(request.headers)  # {'Content-Length': '', 'Content-Type': 'text/plain', 'Host': '192.168.8.130:8081',...
#     print(request.path)  # /hello/
#     print(request.META)  # ...'SSH_CLIENT': '192.168.8.1 1423 22'...
#     print(request.GET)  # <QueryDict: {'year': ['2019'], 'month': ['06']}>
#     data = request.GET
#     year = data.get('year', '2020')
#     month = data.get('month', '1')
#     if request.method == "POST":
#         print(request.method)
#         print(request.body)
#         print(QueryDiec(request.body).dict())
#         print(request.POST)
#         data = request.POST
#         year = data.get('year', '2020')
#         month = data.get('month', '01')
#     return HttpResponse("year is {}, month is {}".format(year, month))
    # return HttpResponse('<p>This is hello index.</p>')

    # 1.普通url参数：http://192.168.8.130:9999/hello/?year=2019&month=06
    # year = request.GET.get("year", "2020")
    # month = request.GET.get("month", "04")
    # print(request)
    # return HttpResponse("year is {}, month is {}".format(year, month))

# 2.位置参数：http://192.168.8.130:9999/hello/2019/06
# def index2(request, month, year):
#     return HttpResponse("year is {}, month is {}".format(year, month))

# 3.可变关键字参数
# def index2(request, **kwargs):
#     print(kwargs)  # 是个字典，{'year': '2019', 'month': '06'}
#     year = kwargs.get('year')
#     month = kwargs.get('month')
#     return HttpResponse("year is {}, month is {}".format(year, month))

# 4.关键字参数：http://192.168.8.130:9999/hello/2019/06，结合url的re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/"...),
# def index2(request, month, year):
#     return HttpResponse("year is {}, month is {}".format(year, month))

