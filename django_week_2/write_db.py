#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops.settings')
django.setup()

from hello.models import User

# 写入数据库
# data = [{"name":"tom", "password":"tom@123"},{"name":"jerry", "password":"jerry@123"}]
# for i in data:
#     User.objects.create(**i)
# User.objects.create(name='david',password='david@123')

# data = {"name":"mary", "password":"mary@123"}
# User.objects.filter(id=3).update(**data)

# print(User.objects.all().values('name', 'password'))
# print(User.objects.all())  # <QuerySet [<User: tom>, <User: jerry>, <User: mary>]>  QuerySet
# print(User.objects.filter(name='tom')) # <QuerySet [<User: tom>]> 列表嵌套QuerySet

# print(User.objects.filter(id=1).values()) # <QuerySet [{'id': 1, 'name': 'tom', 'password': 'tom@123', 'sex': None}]>

#     students_dict['id_delete'] = "/deletestudent/" + str(x.id)
#     students_dict['id_edit'] = "/editstudent/" + str(x.id)
#
# for i in User.objects.values():
#     i['id_delete']="/deleteuser/" + str(i['id'])
#     i['id_edit'] = "/edituser/" + str(i['id'])
#     print(i)
# d = {'id': 1, 'username': '马哥', 'password': 'mage@123', 'sex': 0}
# d[]

# print(User.objects.values().filter(id=14).get(id=14))

# for i in User.objects.values().filter(id=14): # <QuerySet [{'id': 14, 'username': '马爷', 'password': 'mage@123', 'sex': 0}]>
#     print()

x = User.objects.values().filter(id=14)[0]
print(type(x), x)