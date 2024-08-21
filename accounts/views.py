from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .forms import CustomerForm
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

def products(requests):
    products = Product.objects.all()
    return render(requests, 'accounts/products.html', {'products': products})

def customer(requests, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    orders_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'orders_count':orders_count}
    return render(requests, 'accounts/customer.html', context)


def createOrder(request):
    form = OrderForm()
    context = {'form':form}

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/order_forms.html', context)


def createCustomer(requests):
    form = CustomerForm()
    context = {'form':form}

    if requests.method == 'POST':
        # print('Printing POST:', requests.POST)
        form = CustomerForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(requests, 'accounts/customer_forms.html', context)


def update(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_forms.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete_order.html', context)