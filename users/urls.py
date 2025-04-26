from django.urls import path
from .views import home_view,story_view,about_view,contact_view,subscribe_newsletter

urlpatterns = [
    path('', home_view, name='home'),
    path('story/', story_view, name='story'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
]
