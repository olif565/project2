from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm, SignUpFormUser
from django.shortcuts import render, redirect
from django.contrib import messages
import logging

from .models import Profile

logger = logging.getLogger(__name__)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    # Session
                    db = Profile.objects.filter(id=user.profile.pk)
                    if len(db) > 0:
                        request.session['username'] = request.POST['username']
                        request.session['first_name'] = db[0].first_name
                        request.session['status'] = db[0].status
                        request.session['email'] = db[0].email

                    return redirect('home:index')
            else:
                messages.error(request, 'username or password incorrect')
                return redirect('login_view')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpFormUser(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = form.save()
                user.refresh_from_db()
                user.profile.username = form.cleaned_data.get('username')
                user.profile.first_name = form.cleaned_data.get('first_name')
                user.profile.last_name = form.cleaned_data.get('last_name')
                user.profile.email = form.cleaned_data.get('email')
                user.profile.status = '2'
                user.save()

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')

                user = authenticate(username=username, password=password)

                login(request, user)

                # Session
                db = Profile.objects.filter(id=user.profile.pk)
                if len(db) > 0:
                    request.session['username'] = request.POST['username']
                    request.session['first_name'] = db[0].first_name
                    request.session['status'] = db[0].status
                    request.session['email'] = db[0].email

                return redirect('home:index')

    form = SignUpFormUser()
    return render(request, 'signup.html', {'form': form})

