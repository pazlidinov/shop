from django.urls import path

from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('detail/<pk>', views.ProductDetailView.as_view(), name='detail'),
    path("delete/comment/<int:comment_id>", views.delete_comment, name='delete_comment'),
    path('create_comment/<pk>', views.create_comment, name='create_comment'),
    path('add/rating/', views.add_rating, name="add_rating"),
    
    # sort
    path('sort/', views.sort_products, name="sort_products"),

]
