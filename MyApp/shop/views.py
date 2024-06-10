from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Your product will be display here.')
def addNew(request):
    return HttpResponse('Please enter new product.')