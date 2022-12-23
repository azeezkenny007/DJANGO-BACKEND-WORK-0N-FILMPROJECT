from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def authenticate(func):
    def inner(request):
        if request.user.is_authenticated:
            return func(request)
        else:
            return redirect('signin')
    return inner
