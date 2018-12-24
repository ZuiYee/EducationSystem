from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth



def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'web/profile.html')
