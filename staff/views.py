# !/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request):
    pass


def log_in(request):
    errors = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:

                user = get_object_or_404(User, username=username)
                login(request, user)
                return redirect("http://www.baidu.com")
                # if user.department == "":
                #     return redirect(request, "/product/")
                # elif user.department == "":
                #     return redirect(request, "/market/")
                # elif user.department == "":
                #     return redirect(request, "/repository/")
            else:
                errors = "用户名或密码错误"
    else:
        form = LoginForm()
    return render(
        request,
        'staff/login.html',
        {
            "errors": errors,
            "form": form,
            "user": request.user
        }
    )