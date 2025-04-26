from django.shortcuts import render

def products_view(request):
    return render(request, 'products/products.html')

def product_detail_view(request):
    return render(request, 'prodcuts/product_detail.html')