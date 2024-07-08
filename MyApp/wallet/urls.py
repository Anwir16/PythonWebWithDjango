from django.urls import path
from . import views

app_name = 'wallet'

urlpatterns = [
    path('buy/',views.payment, name='buy_point'),
    path('history/', views.payment_history, name='payment_history'),
]
