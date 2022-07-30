from django.shortcuts import render
from django.db.models import Q

from products.models import Product
from cart.models import Cart
from category.models import Category

def productListView(request, pk):
    if pk !='search':
        products = Product.objects.filter(category__category = pk, status = 1).order_by('-id')
        all_category = Category.objects.all()

        context = {
            'products' : products,  
            'all_category' : all_category
            }

        return render(request, 'user/product_list.html', context)
    else:

        # ============= product search ==============
        
        search_input = request.GET.get('search_input')
        products = Product.objects.filter(Q(name__icontains = search_input) | Q(title__icontains = search_input))
        all_category = Category.objects.all()
        
        context = {
        'products' : products, 
        'all_category' : all_category
        }

        return render(request, 'user/product_list.html', context)

def productDetailsView(request, pk):
    product = Product.objects.get(id = pk)
    try:
        Cart.objects.get(product = product, user = request.user)
        alredy_in_cart = True
    except:
        alredy_in_cart = False

    discount = round((product.marking_price - product.selling_price) * (100/product.marking_price),1)

    context = {
    'product' : product, 
    'discount' : discount, 
    'alredy_in_cart' : alredy_in_cart, 
    }

    return render(request, 'user/product_details.html', context)

