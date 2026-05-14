from django.shortcuts import get_object_or_404, render
from .models import Contact, Order, Product
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
        desc = request.POST.get('query', '')
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
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        # Assuming the Order model has an 'order_id' field as primary key
        return render(request, 'shop/order_confirmation.html')
    else:
        return render(request, 'shop/checkout.html')



    return render(request, 'shop/checkout.html')