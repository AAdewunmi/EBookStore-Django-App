from django.shortcuts import render

# Create your views here.
from .models import Category, Product

def categories(request):
    return{
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})