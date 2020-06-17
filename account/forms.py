from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Fisrt Name', max_length=30,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=150,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(label='Username', max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label='Password', max_length=30,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password Confirmation', max_length=30,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', max_length=20,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')