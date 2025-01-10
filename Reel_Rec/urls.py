"""
URL configuration for Reel_Rec project.
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    # APP URLS
    path('', views.home,  name='home'),
    path('signedin/', views.home, name='signedin'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('updates/', views.changelog, name='changelog'),
    path('recommendations/', views.rrec, name='rrec'),
    
    # AUTH URLS
    path('reel-rec/admin/', admin.site.urls),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signin/', auth_views.LoginView.as_view(template_name='auth/signin.html'), name='signin'),
    path('accounts/signout/', auth_views.LogoutView.as_view(template_name='auth/index.html'), name='signout'),
    path('accounts/account/', views.profile, name='profile'),
    path('accounts/change_pass/', auth_views.PasswordChangeView.as_view(template_name='auth/pass_change.html'), name='change_pass'),
    path('accounts/change_pass/done/', auth_views.PasswordChangeDoneView.as_view(template_name='auth/pass_change_done.html'), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]

# Error Handlers
handler404 = views.page_not_found
handler500 = views.server_error