from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    # path('login/', views.my_login, name='my_login'),

    path("login/", auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    path("logout/", auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path("register/", views.my_register_view, name='register'),

]
