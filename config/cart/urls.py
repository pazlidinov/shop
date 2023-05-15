from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.idex_cart, name='index_cart')
]
