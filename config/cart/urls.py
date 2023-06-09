from django.urls import path 
from . import views 


app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/<int:product_id>', views.AddToCartView, name='add_to_cart'),
    
    # Cart
    path('cart/delete/', views.cart_delete, name='cart_delete'),
    path('cart/remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('update/<str:key_update>', views.cart_item_update, name='cart_item_update'),
    
    # Liked
    path('liked/', views.LikedView, name='liked'),
    path('liked/add/<int:product_id>', views.AddToLikedView, name='add_to_liked'),
    path('liked/remove/<int:id>', views.liked_remove, name='liked_remove'),

]
