import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def reg_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        user = authenticate(request, username=user.username, password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, "reg.html", {
                'error': "Invalid credentials",
                'username': request.POST['username']
            })
    else:
        return render(request, 'reg.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, "login.html", {
                'error': "Invalid credentials",
                'username': request.POST['username']
            })
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')