from django.shortcuts import render, redirect
from .forms import CustumUserCreationForm, CustumAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustumUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustumUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts_form.html', context)

def login(request):
    if request.method == 'POST':
        form = CustumAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

    else:
        form = CustumAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def profile(request, username):
    user_info = User.objects.get(username=username)

    context = {
        'user_info': user_info,
    }

    return render(request, 'profile.html', context)