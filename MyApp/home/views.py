from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:login') #use decorator
def dashboard(request):
    return render(request,'home/dashboard.html')

def view_404(requests, exception):
    return render(requests, 'home/404.html', status=404)

def view_403(requests, exception):
    return render(requests, 'home/403.html', status=403)

def view_500(requests):
    return render(requests, 'home/500.html', status=500)

def csrf_failure(request, reason=""):
    return render(request, 'home/403.html', status=403)