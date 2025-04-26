from django.db import models
from config.models import BasedModel

class NewsletterSubscription(BasedModel):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email