from django.shortcuts import render
from .models import Order, OrderItem

# Create your views here.
def order_list(request):
    orders = Order.objects.filter(completed=False)
    orderItems = OrderItem.objects.all()
    return render(request, 'orders/order_list.html', {'orders':orders,'orderItems':orderItems})
