from django.shortcuts import render

# Create your views here.
def start_game(request):
    return render(request, 'game/start.html')