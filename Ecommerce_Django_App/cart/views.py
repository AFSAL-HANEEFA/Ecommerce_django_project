from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from products.models import Product
from cart.models import Cart


@login_required(login_url='account:login')
def addToCartView(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id = product_id)
        Cart.objects.create(user = request.user, product = product)
        data = { 
            'status' : 'Product added successfully'
        }
        return JsonResponse(data)

@login_required(login_url='account:login')
def addToCartBeforeLoginView(request, pk):
    product = Product.objects.get(id = pk)
    cart = Cart.objects.filter(product = product, user = request.user)
    if cart:
        return redirect('products:product_details', pk=str(pk))
    else:
        Cart.objects.create(user = request.user, product = product)
        return redirect('products:product_details', pk=str(pk))

@login_required(login_url='account:login')
def cartView(request):
    # =========== product revove from cart =============
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart_product = Cart.objects.get(user = request.user, product = product_id)
        cart_product.delete()
        return JsonResponse({'status' : 'Product removed from cart'})

    carts = Cart.objects.filter(user = request.user)
    no_of_items = carts.count()
    total_marking_price =0
    total_amount = 0
    for cart in carts:
        total_marking_price += cart.product.marking_price * cart.qty
        total_amount = total_amount + (cart.product.selling_price * cart.qty)
    discount = total_marking_price - total_amount
    cart = Cart.objects.filter(user = request.user)

    context = {
    'cart' : cart,
    'no_of_items' : no_of_items,
    'total_marking_price' : total_marking_price,
    'discount' : discount,
    'total_amount' : total_amount,
    }

    return render (request, 'user/cart.html', context)

def changeQtyView(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        qty = request.POST.get('quantity')
        cart = Cart.objects.get(user = request.user, product = product_id)
        cart.qty = qty
        cart.save()
        return JsonResponse({'status' : 'qty changed successfully'})