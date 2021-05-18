from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


def redirect_user(request):
    return redirect('/accounts/login')


def logout_user(request):
    logout(request)
    return redirect('/')


def login_form(request):
    return render(request, 'accounts/login.html', {})


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            login(request, user)
            return redirect('/')
    return redirect('/accounts/login', request)


def signup_form(request):
    pass


def signup_user(request):
    pass
