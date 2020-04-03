#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.db import models

# 创建数据库表
class User(models.Model):
    sex = (('0', '男'), ('1', '女'))
    username = models.CharField(max_length=20, help_text='用户名')
    password = models.CharField(max_length=32, help_text='密码')
    sex = models.IntegerField(choices=sex, null=True, blank=True)

    # def __str__(self):
    #     return self.username

