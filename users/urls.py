from django.urls import path
from .views import home_view,shop_view,product_view,story_view,about_view,cart_view,contact_view,checkout_view,thanks_view

urlpatterns = [
    path('', home_view, name='hello_world'),
    path('shop/', shop_view, name='shop'),
    path('product/', product_view, name='product'),
    path('story/', story_view, name='story'),
    path('about/', about_view, name='about'),
    path('cart/', cart_view, name='cart'),
    path('contact/', contact_view, name='contact'),
    path('checkout/', checkout_view, name='checkout'),
    path('orderplaced/', thanks_view, name='thanks'),
]
