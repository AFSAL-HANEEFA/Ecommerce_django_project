from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import random
from django.conf import settings
from django.contrib import messages
from profiles.form import AddressForm

from profiles.models import CustomerAddress
from cart.models import Cart
from products.models import Product
from orders.models import Order
from offers.models import Coupon

@login_required(login_url='account:login')
def singleOrderView(request, pk):

        # =========== check is there any default address =============

    try:
        is_default_address = CustomerAddress.objects.get(user = request.user, default = True)

        if request.method == 'POST':
            prod = request.POST.get('product')
            product = Product.objects.get(id = prod)
            cost = product.cost_price
            qty = int(request.POST.get('qty'))
            total_cost = cost*int(qty)
            total_amount = request.POST.get('total_amount')
            payment = request.POST.get('payment')
            payment_id = request.POST.get('payment_id')
            tracking_id = str(request.user.username) + str(random.randint(1111, 9999))

            while Order.objects.filter(tracking_id = tracking_id) is None:
                tracking_id = str(request.user) + str(random.randint(111111, 999999))

            product.qty = product.qty - qty
            product.save()
            order  = Order()

            try:
                coupon = Coupon.objects.get(id = request.session.get('coupon_id'), is_active = True, is_redeemed = False)
                order.coupon = coupon.discount
                order.total_amount = (product.selling_price * qty) - int(coupon.discount)
                del request.session['coupon_id']
                del request.session["coupon_discount"]
                coupon.is_redeemed = True
                coupon.save()
            except:
                order.total_amount = (product.selling_price * qty)

            order.total_cost = total_cost
            order.user = request.user.username
            order.address = is_default_address
            order.product = product
            order.product_id = product.id
            order.image = product.image1
            order.product_selling_price = product.selling_price
            order.qty = qty
            order.payment = payment

            if payment_id:
                order.payment_id = payment_id
            order.tracking_id = tracking_id
            order.status = 'success'
            order.save()

            # ============== delete ordered items from cart =============

            orders = Order.objects.filter(user = request.user)

            for order in orders:
                try:
                    ordered_items_also_in_cart =  Cart.objects.filter(user = request.user, product__id = order.product_id)
                    ordered_items_also_in_cart.delete()
                except:
                    pass
            
            messages.success(request, 'Congratulation! Your order placed successfuly')
            return redirect('orders:your_order')

        address = is_default_address
        addresses = CustomerAddress.objects.filter(user = request.user).order_by('-id')
        form = AddressForm
        product = Product.objects.get(id = pk)

        try:
            cart = Cart.objects.get(user = request.user, product = product)
            qty = cart.qty
        except:
            qty = 1

        marking_price = product.marking_price * qty
        selling_price = product.selling_price * qty
        discount = marking_price - selling_price

        if(request.session.get('coupon_discount')):
            special_offer = request.session.get('coupon_discount')
            total_amount =selling_price-special_offer
            remove_coupon = True
        else:
            special_offer = False
            remove_coupon = False
            total_amount = selling_price

        context = {
        'address' : address, 
        'form' : form, 
        'addresses' : addresses, 
        'qty' : qty,
        'total_marking_price' : marking_price, 
        'discount' : discount, 
        'special_offer' : special_offer, 
        'remove_coupon' : remove_coupon, 
        'total_amount' : total_amount, 
        'product' : product,
        }

        return render(request, 'user/checkout.html', context)

    except:
        messages.info(request, 'Add address or make sure there is a default address to continue your order')
        return redirect('profiles:customer_profile')

@login_required(login_url='account:login')
def cartOrderView(request):
    
        # =========== check is there any default address =============

    try:
        is_default_address = CustomerAddress.objects.get(user = request.user, default = True)
        if request.method == 'POST':

            cart = Cart.objects.filter(user = request.user)

            for cart in cart:
                product = cart.product
                qty = cart.qty
                cost = product.cost_price
                total_cost = cost*qty
                total_amount = request.POST.get('total_amount')
                payment = request.POST.get('payment')
                payment_id = request.POST.get('payment_id')
                tracking_id = str(request.user) + str(random.randint(1111, 9999))

                while Order.objects.filter(tracking_id = tracking_id) is None:
                    tracking_id = str(request.user) + str(random.randint(111111, 999999))

                product.qty = product.qty - int(qty)
                product.save()
                order  = Order()

                try:
                    coupon = Coupon.objects.get(id = request.session.get('coupon_id'), is_active = True, is_redeemed = False)
                    order.coupon = coupon.discount
                    order.total_amount = (product.selling_price * qty) - int(coupon.discount)
                    del request.session['coupon_id']
                    del request.session["coupon_discount"]
                    coupon.is_redeemed = True
                    coupon.save()
                except:
                    order.total_amount = (product.selling_price * qty)

                order.total_cost = total_cost
                order.user = request.user.username
                order.address = is_default_address
                order.product = product
                order.product_id = product.id
                order.image = product.image1
                order.product_selling_price = product.selling_price
                order.qty = qty
                order.payment = payment

                if payment_id:
                    order.payment_id = payment_id
                order.tracking_id = tracking_id
                order.status = 'success'
                order.save()
                cart.delete()
            messages.success(request, 'Congratulation! Your order placed successfuly')
            return redirect('orders:your_order')

        address = is_default_address
        addresses = CustomerAddress.objects.filter(user = request.user).order_by('-id')
        form = AddressForm
        carts = Cart.objects.filter(user = request.user)
        no_of_items = carts.count()
        total_marking_price =0
        amount = 0

        for cart in carts:
            total_marking_price += cart.product.marking_price * cart.qty
            amount = amount + (cart.product.selling_price * cart.qty)
        discount = total_marking_price - amount

        if(request.session.get('coupon_discount')):
            special_offer = request.session.get('coupon_discount')
            total_amount =amount-special_offer
            remove_coupon = True
        else:
            special_offer = False
            remove_coupon = False
            total_amount = amount

        context = {
        'address' : address, 
        'form' : form, 
        'addresses' : addresses, 
        'no_of_items' : no_of_items,
        'total_marking_price' : total_marking_price, 
        'discount' : discount, 
        'remove_coupon' : remove_coupon, 
        'total_amount' : total_amount, 
        'cart' : carts,
        'special_offer' : special_offer
        }

        return render(request, 'user/checkout.html', context)

    except:
        messages.info(request, 'Add address or make sure there is a default address to continue your order')
        return redirect('profiles:customer_profile')


@login_required(login_url='account:login')
def yourOrderView(request):
    orders = Order.objects.filter(user = request.user.username).order_by('-id')

    context = {
        'orders' : orders, 
        }
    
    return render(request, 'user/your_order.html', context)

@login_required(login_url='account:login')
def paymentView(request):
    carts = Cart.objects.filter(user = request.user)
    total_amount = 0
    for cart in carts:
        total_amount = total_amount + (cart.product.selling_price * cart.qty)
    address = CustomerAddress.objects.get(user = request.user, default = True)
    name = address.name
    mob = address.mob
    return JsonResponse({
        'total_amount' : total_amount, 
        'name' : name, 'mob' : mob
        })

@login_required(login_url='account:login')
def razorpayKey(request):
    data = {'key' : settings.RAZORPAY_API_KEY}
    return JsonResponse(data)