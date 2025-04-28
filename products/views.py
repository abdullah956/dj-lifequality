from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def products_view(request):
    sort = request.GET.get('sort')
    products = Product.objects.all()
    if sort == 'low':
        products = products.order_by('price')
    elif sort == 'high':
        products = products.order_by('-price')
    categories = Category.objects.all()
    return render(request, 'products/products.html', {'products': products, 'categories': categories})

def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product})


def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'products/products.html', {'products': products, 'categories': categories, 'selected_category': category})

def products_by_category(request, category_id):
    sort = request.GET.get('sort')
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    
    if sort == 'low':
        products = products.order_by('price')
    elif sort == 'high':
        products = products.order_by('-price')
        
    return render(request, 'products/products.html', {'category': category, 'products': products})
