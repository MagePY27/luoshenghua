#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from hello.forms import UserForm,EditUserForm
from hello.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


def adduser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            s = User(username=request.POST.get('username'),
                     password=request.POST.get('password'),
                     sex=request.POST.get('sex'),
                     )
            s.save()

            return HttpResponseRedirect('/showuser')
        else:
            return render(request, 'adduser.html', {'form':form})
    else:
        form = UserForm()
        return render(request, 'adduser.html', {'form':form})

def showuser(request):
    users_list = []
    for i in User.objects.values():
        i['id_delete'] = "/deleteuser/" + str(i['id'])
        i['id_edit'] = "/edituser/" + str(i['id'])
        users_list.append(i)
    return render(request, 'showuser.html', {'users_list':users_list})

def deleteuser(request, id):
    d = User.objects.all().get(id=id)
    d.delete()
    return HttpResponseRedirect("/showuser")

def edituser(request, id):
    if request.method == 'POST':
        form = EditUserForm(request.POST)

        if form.is_valid():
            x = User.objects.get(id=id)
            x.username = request.POST.get('username')
            x.password = request.POST.get('password')
            x.sex = request.POST.get('sex')
            x.save()

            return HttpResponseRedirect('/showuser')
        else:
            return render(request, 'edituser.html', {'form':form})
    else:
        form = EditUserForm(initial=User.objects.values().filter(id=id).get(id=id))
        return render(request, 'edituser.html', {'form':form})