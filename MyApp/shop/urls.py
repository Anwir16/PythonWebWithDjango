from . import views
from django.urls import path
app_name = 'shop'
urlpatterns = [
    path('',views.dashboard, name='home'),
]