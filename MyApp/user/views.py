from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from .models import UserRegistration
# Create your views here.
def register_user(request):
    context = {
        'csrf_token': get_token(request),
    }
    return render(request, 'login_register.html', context)


def register_process(request):
    if request.method == 'POST':

        _email = request.POST.get('email')
        print(f'email: {_email}')
        _password = request.POST.get('password')
        print(f'password: {_password}')
        _username = request.POST.get('username')
        print(f'username: {_username}')
        _fullname = request.POST.get('fullname')
        print(f'fullname: {_fullname}')
        obj_userregistration = UserRegistration(user_name=_username,email=_email, password=_password,full_name=_fullname)
        obj_userregistration.save()
        if obj_userregistration.save():
            print('Success')
        return HttpResponseRedirect('shop:dashboard.html')    
    else:
        return redirect('')