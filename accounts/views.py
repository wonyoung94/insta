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

def follows(request, username):
    me = request.user
    you = User.objects.get(username=username)

    #이미 팔로잉이 되어있는 경우
    if you in me.followings.all(): # 내 팔로잉 목록에 너가 있는지?
    # if me in you.followers.all(): # 니 팔로우 목록에 내가 있는지?
        me.followings.remove(you)
    # 아직 팔로잉이 안된 경우
    else:
        me.followings.add(you)

    return redirect('accounts:profile', username=username)