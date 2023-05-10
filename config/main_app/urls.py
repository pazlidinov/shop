from django.urls import path

from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('detail/<pk>', views.ProductDetailView.as_view(), name='detail'),
    path("delete/comment/<int:comment_id>", views.delete_comment, name='delete_comment'),
    path('create_comment/<pk>', views.create_comment, name='create_comment'),
]
