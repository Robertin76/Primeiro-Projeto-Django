from django.shortcuts import render
from django.http import HttpResponse
from models import *

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def products(requests):
    products = Product.object.all()
    return render(requests, 'accounts/products.html', {'products': products})

def customer(requests):
    return render(requests, 'accounts/customer.html')

