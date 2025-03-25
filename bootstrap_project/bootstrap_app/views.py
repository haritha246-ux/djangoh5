from django.shortcuts import render
from .models import Product
def home(request):
    return render(request,'home.html')
def product_list(request):
    if not Product.objects.exists():
        Product.objects.create(name='Sugar',description='Good Quality',price='1200')
        Product.objects.create(name='Groundnuts',description='Low quality',price='700')
        Product.objects.create(name='Chocolates',description='Excellent',price='150')
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})