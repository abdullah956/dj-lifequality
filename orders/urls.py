from django.urls import path
from .views import orders_view,update_order_status,order_detail_view,download_orders_excel

urlpatterns = [
    path('orders/', orders_view, name='orders'),
    path('orders/<int:order_id>/update-status/', update_order_status, name='update_order_status'),
    path('orders/<int:id>/detail/', order_detail_view, name='order_detail'),
     path('orders/download/', download_orders_excel, name='download_orders_excel'),
]
