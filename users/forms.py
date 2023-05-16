from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


"""Определение полей для входа пользователя"""
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password')


"""Переопределение виджета"""
class DateInput(forms.DateInput):
    input_type = 'date'


"""Определение полей для регистрации пользователя"""
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта'}))
    date_birth = forms.DateField(widget=DateInput())
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'date_birth', 'password1', 'password2')