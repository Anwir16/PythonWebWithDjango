from . import views
from django.urls import path
app_name = 'user'
urlpatterns = [
    path('login/',views.loginViews, name='login'),
    path('register/',views.signup, name='register'),
    path('signout/',views.logoutViews, name='signout'),
]