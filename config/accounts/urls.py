from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    
    path("login/", auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    
    path("logout/", auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path("register/", views.my_register_view, name='register'),
    path('contact/', views.Contact.as_view(), name='contact'),

]
