from django.shortcuts import render

def checkout_view(request):
    return render(request, 'checkouts/checkout.html')

def thanks_view(request):
    return render(request, 'checkouts/thanks.html')