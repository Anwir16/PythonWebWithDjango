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
    #path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('password-reset/', PasswordResetView.as_view(success_url=reverse_lazy('user:password_reset_done')),name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url=reverse_lazy('user:password_reset_complete')),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]