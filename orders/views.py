from django.shortcuts import render , get_object_or_404, redirect
from checkouts.models import Order
from datetime import datetime
import openpyxl
from django.http import HttpResponse
from products.models import Product
from django.core.mail import send_mail
from config import settings

def orders_view(request):
    filter_date = request.GET.get('filter_date')
    orders = Order.objects.all().order_by('-created_at')
    if filter_date:
        try:
            date_obj = datetime.strptime(filter_date, '%Y-%m-%d').date()
            orders = orders.filter(created_at__date=date_obj).order_by('-created_at')
        except ValueError:
            pass
    return render(request, 'orders/orders_list.html', {
        'orders': orders,
        'status_choices': Order.ORDER_STATUS
    })


def update_order_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        if new_status in dict(Order.ORDER_STATUS):
            order.status = new_status
            order.save()
            send_mail(
            subject='Update on Your Order Status',
            message=(
                f'Dear {order.first_name},\n\n'
                f'Thank you for shopping with us. We would like to inform you that the status of your order #{order.id} '
                f'has been updated to **{new_status.capitalize()}**.\n\n'
                f'If you have any questions, feel free to contact our support team.\n\n'
                f'Best regards,\nYour Company Name'
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[order.email],
            fail_silently=False,
            )

    return redirect('orders')


def order_detail_view(request, id):
    order = get_object_or_404(Order, id=id)
    cart_items = []
    if isinstance(order.cart_data, dict):
        for product_id, qty in order.cart_data.items():
            try:
                product = Product.objects.get(id=product_id)
                price = product.sale_price if product.sale_price else product.price
                cart_items.append({
                    'name': product.name,
                    'price': price,
                    'quantity': qty,
                    'subtotal': price * qty,
                    'image': product.image.url if product.image else ''
                })
            except Product.DoesNotExist:
                continue
    return render(request, 'orders/order_detail.html', {'order': order, 'cart_items': cart_items})


def download_orders_excel(request):
    filter_date = request.GET.get('filter_date')
    orders = Order.objects.all()
    if filter_date:
        try:
            date_obj = datetime.strptime(filter_date, '%Y-%m-%d').date()
            orders = orders.filter(created_at__date=date_obj)
        except ValueError:
            pass
    if not orders:
        return HttpResponse("No orders found for the selected date.", content_type="text/plain")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Orders"
    ws.append(["ID", "Name", "Email", "Total", "Status", "Paid", "Date"])

    for o in orders:
        ws.append([
            o.id,
            f"{o.first_name} {o.last_name}",
            o.email,
            str(o.total_amount),
            o.status,
            "Yes" if o.paid else "No",
            o.created_at.strftime('%Y-%m-%d'),
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=orders.xlsx'
    wb.save(response)
    return response