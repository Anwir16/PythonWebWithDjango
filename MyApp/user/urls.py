from . import views
from django.urls import path
app_name = 'user'
urlpatterns = [
    path('',views.register_user, name='login'),
    path('register/',views.register_process, name='register'),
]