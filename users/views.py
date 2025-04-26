from django.shortcuts import render , redirect
from .forms import NewsletterSubscriptionForm

def home_view(request):
    return render(request, 'users/home.html')

def story_view(request):
    return render(request, 'users/story.html')

def about_view(request):
    return render(request, 'users/about.html')

def contact_view(request):
    return render(request, 'users/contact.html')

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))
