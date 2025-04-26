from django.urls import path
from .views import products_view,product_detail_view
urlpatterns = [
    path('', products_view, name='shop'),
    path('product/', product_detail_view, name='product'),
    
]
