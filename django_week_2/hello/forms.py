#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django import forms

# 创建添加用户的表单
class UserForm(forms.Form):
    required_css_class = 'required'

    username = forms.CharField(max_length=20, min_length=2,label="用户名",
                               required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32,min_length=6,label="密码",
                               required=True, widget=forms.TextInput(attrs={'class':'form-control'}) )
    sex_choices = (('0', '男'), ('1', '女'))
    sex = forms.IntegerField(required=False, widget=forms.Select(choices=sex_choices, attrs={'class':'form-control'}))

# 创建修改用户的表单
class EditUserForm(UserForm):
    id = forms.CharField(label='用户唯一ID', widget=forms.TextInput(attrs={"class": "form-control", 'readonly': True}))
