from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Your First name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)
    class Meta:
        model = User
        fields = ['username','first_name','last_name' ,'email', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['organization']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Your First name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['organization']