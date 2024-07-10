from . import views
from django.urls import path

app_name = 'game'
urlpatterns = [
    path('start/',views.start_game, name='start'),
    path('round/', views.play_round, name='play_round'),
]