from .forms import UserUpdateForm, UpdateProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        u_form = UserCreationForm(request.POST)
        if u_form.is_valid():
            user = u_form.save()
            Profile.objects.create(user=user)
            username = u_form.cleaned_data.get('username')
            password = u_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/signup.html', {'u_form': u_form})
    else:
        u_form = UserCreationForm()
        return render(request, 'user/signup.html', {'u_form': u_form})
    
def loginViews(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = 'Invalid username or password'
            u_form = AuthenticationForm()
            return render(request, 'user/login.html', {'u_form': u_form, 'error': error})
    else:
        u_form = AuthenticationForm()
    return render(request, 'user/login.html', {'u_form': u_form})

@login_required(login_url='user/login/')
def logoutViews(request):
    logout(request)
    return redirect('user:login')

@login_required(login_url='user/login/')
def viewsProfile(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    return render(request,'user/profile.html')

@login_required(login_url='user/login/')
def updateProfile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user:profile')
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = UpdateProfileForm(instance=profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile' : profile,
        'choices' : Profile.CHOICES
    }
    
    return render(request, 'user/updateProfile.html',context)
