from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


def authenticate(func):
    def inner(request):
        if request.user.is_authenticated:
            return func(request)
        else:
            return redirect('signin')
    return inner



def is_authenticated(user):
    return user.is_authenticated

def custom_login_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if is_authenticated(request.user):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_func

@custom_login_required
def secret_view(request):
    # Only authenticated users can access this view
    return render(request, 'secret.html')
