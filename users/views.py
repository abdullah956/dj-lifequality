from django.shortcuts import render , redirect
from .forms import NewsletterSubscriptionForm
from products.models import Category, Product, Review
from .models import ContactMessage

def home_view(request):
    categories = Category.objects.all()
    top_reviews = Review.objects.filter(rating=5).order_by('-id')[:5]

    for review in top_reviews:
        avg_rating = int(review.rating) if review.rating else 0
        filled_stars = [True] * avg_rating
        unfilled_stars = [False] * (5 - avg_rating)
        review.filled_stars = filled_stars
        review.unfilled_stars = unfilled_stars

    best_sellers = Product.objects.filter(best_sellers=True)
    new_arrivals = Product.objects.filter(new_arrivals=True)
    hot_sales = Product.objects.filter(hot_sales=True)
    
    return render(request, 'users/home.html', {
        'categories': categories,
        'best_sellers': best_sellers,
        'new_arrivals': new_arrivals,
        'hot_sales': hot_sales,
        'top_reviews': top_reviews,
    })


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

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return render(request, 'users/contact.html')