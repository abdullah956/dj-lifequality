from django.urls import path
from .views import cart_view,add_to_cart,update_cart,remove_from_cart

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update/', update_cart, name='update_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
