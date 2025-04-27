from django.contrib import admin
from .models import NewsletterSubscription, ContactMessage

admin.site.register(NewsletterSubscription)
admin.site.register(ContactMessage)