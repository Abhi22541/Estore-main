from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views
from .forms import UserLoginForm

urlpatterns=[
    path("register/", views.account_register, name="register"),
    path("activate/<slug:uidb64><slug:token>/", views.account_activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("login/", auth_views.LoginView.as_view(template_name='store/accounts/login.html', form_class=UserLoginForm), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='accounts/login/'), name='logout'),
    path('profile/edit/', views.edit_details, name='edit_details'),
]