from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def shop_view(request):
    return render(request, 'shop.html')

def product_view(request):
    return render(request, 'shop-details.html') 

def story_view(request):
    return render(request, 'blog.html')

def about_view(request):
    return render(request, 'about.html')

def cart_view(request):
    return render(request, 'shopping-cart.html')

def contact_view(request):
    return render(request, 'contact.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def thanks_view(request):
    return render(request, 'thanks.html')