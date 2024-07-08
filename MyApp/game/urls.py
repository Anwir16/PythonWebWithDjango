from . import views
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
    path('start/',views.start_game, name='start'),
]