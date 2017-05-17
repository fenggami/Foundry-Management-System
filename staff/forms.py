# _*_ coding:utf-8 _*_
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(widget=forms.PasswordInput, label="密码")


