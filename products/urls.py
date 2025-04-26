from django.urls import path
from .views import products_view,product_detail_view
urlpatterns = [
    path('', products_view, name='products'),
    path('product/', product_detail_view, name='product'),
    
]
