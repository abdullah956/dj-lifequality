from django.urls import path
from .views import products_view,product_detail_view,category_products_view,products_by_category
urlpatterns = [
    path('', products_view, name='products'),
    path('product/<int:id>/', product_detail_view, name='product_detail'),
    path('category/<int:category_id>/', category_products_view, name='category_products'),
    path('products/<int:category_id>/', products_by_category, name='products_by_category')

]
