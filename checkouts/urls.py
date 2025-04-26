from django.urls import path
from .views import checkout_view,thanks_view

urlpatterns = [
    path('checkout/', checkout_view, name='checkout'),
    path('thanks/', thanks_view, name='thanks'),
]
