from django.shortcuts import render
from .models import Order, OrderItem
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def orderList(request):
    orders = Order.objects.filter(completed=False)
    orderItems = OrderItem.objects.all()
    return render(request, 'orders/order_list.html', {'orders':orders,'orderItems':orderItems})

def home(request):
    return render(request, 'orders/home.html', {})

def makeOrder(request):
    return render(request, 'orders/make_order.html')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
    form = RegistrationForm()
    return render(request, 'registration/register.html',{'form': form})
