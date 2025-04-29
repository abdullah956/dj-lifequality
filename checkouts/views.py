from django.shortcuts import render, redirect
from .models import Order
from django.contrib import messages
from decimal import Decimal
from django.http import HttpResponse
from products.models import Product
from django.core.mail import send_mail

def checkout_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        country = request.POST.get('country')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        order_notes = request.POST.get('order_notes')
        cart = request.session.get('cart', {})
        cart_items = []
        cart_total = Decimal('0.00')

        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                price = product.sale_price if product.sale_price else product.price
                item_total = Decimal(price) * Decimal(quantity)
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'total_price': item_total
                })
                cart_total += item_total
            except Product.DoesNotExist:
                continue

        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            country=country,
            address=address,
            city=city,
            state=state,
            postcode=postcode,
            phone=phone,
            email=email,
            order_notes=order_notes,
            total_amount=cart_total,
            cart_data=cart,
            status='pending'
        )
        send_mail(
        subject='Order Confirmation - Thank You for Your Purchase!',
        message=(
            f'Dear {first_name} {last_name},\n\n'
            f'Thank you for your order #{order.id}.\n'
            f'We are currently processing it and will notify you once it ships.\n\n'
            f'Order Summary:\n'
            f'Total Amount: ${cart_total:.2f}\n\n'
            f'Shipping Address:\n{address}, {city}, {state}, {postcode}, {country}\n\n'
            f'If you have any questions, feel free to reply to this email.\n\n'
            f'Best regards,\n'
        ),
        from_email='your_email@gmail.com',
        recipient_list=[email],
        fail_silently=False,
        )
        request.session['cart'] = {}
        messages.success(request, 'Your order has been placed successfully!')
        return redirect('thanks')

    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = Decimal('0.00')

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            price = product.sale_price if product.sale_price else product.price
            item_total = Decimal(price) * Decimal(quantity)
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': item_total
            })
            cart_total += item_total
        except Product.DoesNotExist:
            continue

    return render(request, 'checkouts/checkout.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
    })



def thanks_view(request):
    return render(request, 'checkouts/thanks.html')