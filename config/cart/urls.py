from django.urls import path 
from . import views 


app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('add/<int:product_id>', views.AddToCartView.as_view(), name='add_to_cart'),
    
    path('cart/delete/', views.cart_delete, name='cart_delete'),
    path('cart/remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('cart/update/', views.cart_item_update, name='cart_item_update'),

]
