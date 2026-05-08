from django.shortcuts import render
from math import ceil
from .models import Product


def index(request):
    # Fetch all products from the database
    all_products = Product.objects.all()
    n = len(all_products)
    if n == 0:
        return render(request, 'shop/index.html', {'all_carousels': []})

    # Define how many products per slide (matches col-md-4 for 3 columns)
    items_per_slide = 3
    nSlides = ceil(n / items_per_slide)

    # Group all products into slides
    product_slides = [all_products[i:i + items_per_slide] for i in range(0, n, items_per_slide)]

    # Prepare the data for two carousels, each containing all products
    all_carousels = [
        {'title': 'Featured Products', 'slides': product_slides, 'range': range(nSlides)},
        {'title': 'New Arrivals', 'slides': product_slides, 'range': range(nSlides)}
    ]

    context = {'all_carousels': all_carousels}
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