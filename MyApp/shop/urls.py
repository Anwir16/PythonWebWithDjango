from . import views
from django.urls import path
app_name = 'shop'
urlpatterns = [
    path('login/',views.loginView, name= 'login'),
    path('',views.dashboard, name='home'),
    path('register/',views.register, name= 'register'),
]