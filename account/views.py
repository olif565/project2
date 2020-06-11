from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
import logging


logger = logging.getLogger(__name__)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            logger.error(user)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')
            else:
                messages.error(request, 'username or password incorrect')
                return redirect('login_view')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.username = form.cleaned_data.get('username')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home:data-training')

    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

