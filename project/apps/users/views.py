from bson.objectid import ObjectId
from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return redirect('user/login/')


def login(request):
    return render(request, 'users/login.html')
