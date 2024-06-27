from .forms import UserUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(f'username: {username}')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'user/signup.html', {'form': form})
    
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
            form = AuthenticationForm()
            return render(request, 'user/login.html', {'form': form, 'error': error})
    else:
        print("loi")
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def logoutViews(request):
    logout(request)
    return redirect('user:login')

@login_required
def viewsProfile(request):
    profile = Profile.objects.get(user=request.user)
    if request.user.is_superuser:
        return redirect('/admin/')
    return render(request,'user/profile.html',{'profile':profile})

@login_required
def updateProfile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'user/updateProfile.html', {'form': form})

@login_required
def updateImage(requests, user_id):
    pass