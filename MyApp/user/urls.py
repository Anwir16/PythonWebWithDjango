from . import views
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .decorators import redirect_if_authenticated

app_name = 'user'
urlpatterns = [
    path('login/',redirect_if_authenticated(views.loginViews), name='login'),
    path('register/',redirect_if_authenticated(views.signup), name='register'),
    path('validation/username/',lambda request: views.check_unique(request, 'username'), name='validate_username'),
    path('validation/email/',lambda request: views.check_unique(request, 'email'), name='validate_email'),
    path('validation/first_name/',lambda request: views.check_unique(request, 'first_name'), name='validate_first_name'),
    path('validation/last_name/',lambda request: views.check_unique(request, 'last_name'), name='validate_last_name'),
    path('signout/',views.logoutViews, name='signout'),
    path('profile/',views.viewsProfile, name='profile'),
    path('updateProfile/', views.updateProfile, name='updateProfile'),
    
    #change password
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user/changePassword.html',success_url = reverse_lazy("user:password_change_done")), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='user/passwordChangeDone.html'), name='password_change_done'),
    
    #using email to reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='user/password_reset_form.html',
        email_template_name='user/password_reset_email.html',
        success_url=reverse_lazy('user:password_reset_done')
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html',
        success_url=reverse_lazy('user:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html'
    ), name='password_reset_complete'),
]