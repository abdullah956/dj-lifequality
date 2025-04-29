from django.shortcuts import render,redirect
from products.models import Product
from django.http import JsonResponse

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            price = product.sale_price if product.sale_price else product.price
            total_price = price * quantity
            cart_total += total_price

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': total_price,
                'used_price': price,
            })
        except Product.DoesNotExist:
            pass

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'carts/cart.html', context)


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('cart')
def update_cart(request):
    if request.method == 'POST':
        product_id = str(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id] = quantity
            request.session['cart'] = cart

        try:
            product = Product.objects.get(id=product_id)
            unit_price = product.sale_price if product.sale_price else product.price
            item_total = unit_price * quantity
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        cart_total = 0
        for pid, qty in cart.items():
            p = Product.objects.get(id=pid)
            price = p.sale_price if p.sale_price else p.price
            cart_total += price * qty

        response_data = {
            'item_total': f"{item_total:.2f}",
            'cart_total': f"{cart_total:.2f}",
        }

        if product.sale_price:
            response_data['item_original_price'] = f"{product.price:.2f}"
            response_data['item_sale_price'] = f"{product.sale_price:.2f}"

        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    cart_total = sum(Product.objects.get(id=pid).price * qty for pid, qty in cart.items())
    
    return redirect('cart')