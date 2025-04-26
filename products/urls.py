from django.urls import path
from .views import products_view,product_detail_view,category_products_view
urlpatterns = [
    path('', products_view, name='products'),
    path('product/', product_detail_view, name='product'),
    path('category/<int:category_id>/', category_products_view, name='category_products'),
    
]
