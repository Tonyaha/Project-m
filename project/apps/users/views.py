# from bson.objectid import ObjectId
# from django import forms
# from django.conf import settings
# from django.contrib.auth import authenticate, logout
# from django.contrib.auth.hashers import check_password, make_password
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.mail import send_mail
# from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from project.apps.users.models import Users


# Create your views here.

def index(request):
    return redirect('/user/login/')

def login(request):
    if request.method == 'GET':
        pass
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        Users.create(account, password)
        if Users.get_by_email(account):
            return redirect('/user/login/')
    return render(request, 'users/register.html')
