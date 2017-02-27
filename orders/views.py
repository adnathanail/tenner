from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def orderList(request):
    if request.user.groups.filter(name="Staff").count() == 1:
        orderItems = OrderItem.objects.all()
        orderItemOrderers = [i[0] for i in OrderItem.objects.values_list('orderer')]
        Users = User.objects.all()
        return render(request, 'orders/order_list.html', {'orderItems':orderItems,'Users':Users,'orderItemOrderers':orderItemOrderers})
    else:
        return HttpResponseRedirect('/')

def home(request):
    return render(request, 'orders/home.html', {})

def makeOrder(request):
    error = ''
    if request.method == 'POST':
        form = makeOrderForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.orderer = request.user
            model_instance.save()
            return HttpResponseRedirect('/')
        else:
            error = 'Input invalid';
    form = makeOrderForm()
    return render(request, 'orders/make_order.html',{'form': form, 'error':error})

def register(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
        else:
            error = 'Input invalid';
    form = RegistrationForm()
    return render(request, 'registration/register.html',{'form': form, 'error':error})
