from django.shortcuts import render, get_object_or_404,redirect
from .models import Product, Category, Review
from django.db.models import Avg

def products_view(request):
    sort = request.GET.get('sort')
    products = Product.objects.all()
    if sort == 'low':
        products = products.order_by('price')
    elif sort == 'high':
        products = products.order_by('-price')
    products = products.annotate(avg_rating=Avg('reviews__rating'))
    for product in products:
        avg_rating = int(product.avg_rating) if product.avg_rating else 0
        filled_stars = [True] * avg_rating
        unfilled_stars = [False] * (5 - avg_rating)
        product.filled_stars = filled_stars
        product.unfilled_stars = unfilled_stars
        product.avg_rating = product.avg_rating or 0
    categories = Category.objects.all()
    return render(request, 'products/products.html', {'products': products, 'categories': categories})


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    avg_rating = product.reviews.aggregate(Avg('rating'))['rating__avg']
    avg_rating = int(avg_rating) if avg_rating else 0 
    filled_stars = [True] * avg_rating
    unfilled_stars = [False] * (5 - avg_rating)
    product.filled_stars = filled_stars
    product.unfilled_stars = unfilled_stars
    product.avg_rating = avg_rating
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    return render(request, 'products/product_detail.html', {'product': product, 'related_products': related_products})

def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

    for product in products:
        avg_rating = product.reviews.aggregate(Avg('rating'))['rating__avg']
        avg_rating = int(avg_rating) if avg_rating else 0 
        filled_stars = [True] * avg_rating
        unfilled_stars = [False] * (5 - avg_rating)
        product.filled_stars = filled_stars
        product.unfilled_stars = unfilled_stars
        product.avg_rating = avg_rating

    return render(request, 'products/products.html', {'products': products, 'categories': categories, 'selected_category': category})


def products_by_category(request, category_id):
    sort = request.GET.get('sort')
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    if sort == 'low':
        products = products.order_by('price')
    elif sort == 'high':
        products = products.order_by('-price')

    for product in products:
        avg_rating = product.reviews.aggregate(Avg('rating'))['rating__avg']
        avg_rating = int(avg_rating) if avg_rating else 0
        filled_stars = [True] * avg_rating
        unfilled_stars = [False] * (5 - avg_rating)
        product.filled_stars = filled_stars
        product.unfilled_stars = unfilled_stars
        product.avg_rating = avg_rating

    return render(request, 'products/products.html', {'category': category, 'products': products})

def submit_review(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review')

        Review.objects.create(
            product=product,
            name=name,
            email=email,
            rating=rating,
            review=review_text
        )
        return redirect('home')  
    return redirect('home')
