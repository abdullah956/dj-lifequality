from .forms import NewsletterSubscriptionForm

def newsletter_form(request):
    return {'newsletter_form': NewsletterSubscriptionForm()}
