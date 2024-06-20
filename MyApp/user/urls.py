from . import views
from django.urls import path, include
app_name = 'user'
urlpatterns = [
    path('login/',views.loginViews, name='login'),
    path('register/',views.signup, name='register'),
    path('signout/',views.logoutViews, name='signout'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]