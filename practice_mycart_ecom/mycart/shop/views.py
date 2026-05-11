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
    category_set = set(product.category for product in all_products)
    subcategory_set = set(product.subcategory for product in all_products)


    # Group all products into slides
    
    all_carousels = []

    # Prepare the data for two carousels, each containing all products
    for category in category_set:
        category_products = [product for product in all_products if product.category == category]
        n_category = len(category_products)
        nSlides_category = ceil(n_category / items_per_slide)
        category_slides = [category_products[i:i + items_per_slide] for i in range(0, n_category, items_per_slide)]
        all_carousels.append({'title': category, 'slides': category_slides, 'range': range(nSlides_category)})
    

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