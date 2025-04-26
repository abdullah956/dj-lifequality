from django.shortcuts import render

def products_view(request):
    return render(request, 'products.html')

def product_detail_view(request):
    return render(request, 'product_detail.html') 