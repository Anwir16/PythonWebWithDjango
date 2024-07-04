from django.urls import path
from . import views

app_name = 'wallet'

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('payment_ipn/', views.payment_ipn, name='payment_ipn'),
    path('payment_return/', views.payment_return, name='payment_return'),
    path('query/', views.query, name='query'),
    path('refund/', views.refund, name='refund'),
    path('buy/',views.view_buy_point, name='buy_point'),
    path('history/', views.payment_history, name='payment_history'),
]
