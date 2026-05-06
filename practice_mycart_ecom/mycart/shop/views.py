from django.shortcuts import render

from .models import Product


def index(request):
    # Fetch all products from the database
    all_products = Product.objects.all()

    # This logic groups the products into slides for the carousel
    n = len(all_products)
    product_slides = [all_products[i:i + 3] for i in range(0, n, 3)]

    context = {'product_slides': product_slides}
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html') 

def search(request):
    return render(request, 'shop/search.html')

def productview(request):
    return render(request, 'shop/productview.html')

def checkout(request):
    return render(request, 'shop/checkout.html')