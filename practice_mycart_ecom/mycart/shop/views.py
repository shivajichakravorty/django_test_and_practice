from django.shortcuts import get_object_or_404, render
from .models import Contact, Product
from collections import defaultdict


def index(request):
    # Fetch all products from the database
    all_products = Product.objects.all()

    if not all_products:
        return render(request, 'shop/index.html', {'products_by_category': {}})

    # Group products by category
    products_by_category = defaultdict(list)
    for product in all_products:
        products_by_category[product.category].append(product)

    context = {'products_by_category': dict(products_by_category)}
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    else:
        pass
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html') 

def search(request):
    return render(request, 'shop/search.html')

def productview(request, myid):
    product = get_object_or_404(Product, id=myid)
    return render(request, 'shop/productview.html', {'product': product})

def checkout(request):
    return render(request, 'shop/checkout.html')