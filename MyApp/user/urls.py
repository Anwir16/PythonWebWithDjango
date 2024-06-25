from . import views
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import ( 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
app_name = 'user'
urlpatterns = [
    path('login/',views.loginViews, name='login'),
    path('register/',views.signup, name='register'),
    path('signout/',views.logoutViews, name='signout'),
    path('profile/',views.viewsProfile, name='profile'),
    
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]