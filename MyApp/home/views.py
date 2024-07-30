from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:login') #use decorator
def dashboard(request):
    return render(request,'home/dashboard.html')

def view_404(requests, exception):
    return render(requests, 'home/404.html', status=404)
