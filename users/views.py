from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileRegisterForm
from .models import Profile
from django.contrib.auth.forms import  UserChangeForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now Log in')
            return redirect('login')
    else:        
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_forms = UserUpdateForm(request.POST, instance=request.user)
        p_forms = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if u_forms.is_valid() and p_forms.is_valid():
            u_forms.save()
            p_forms.save()
            messages.success(request, f'Your account has been Changed!')
            return redirect('profile')
    else:
        u_forms = UserUpdateForm(instance=request.user)
        p_forms = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_forms,
        'p_form': p_forms
    }
    
    return render(request, 'users/profile.html',context)
