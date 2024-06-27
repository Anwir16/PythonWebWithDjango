from . import views
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
    path('login/',views.loginViews, name='login'),
    path('register/',views.signup, name='register'),
    path('signout/',views.logoutViews, name='signout'),
    path('profile/',views.viewsProfile, name='profile'),
    path('update/<int:user_id>/', views.update, name='update'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='password_reset_email.html',
        success_url=reverse_lazy('user:password_reset_done')
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('user:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]