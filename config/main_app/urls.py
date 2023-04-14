from django.urls import path

from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('detail/<pk>', views.ProductDetailView.as_view(), name='detail'),
]
