from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView
from .forms import (UserLoginForm, PwdResetForm)

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    # Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="account/user/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='account/user/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),
    # User dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.edit_details, name='edit_details'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="account/user/delete_confirm.html"), name='delete_confirmation'),
]
