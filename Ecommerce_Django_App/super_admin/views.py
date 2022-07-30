from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import View
from super_admin.form import CategoryDetailsForm, ProductDetailsForm, CouponForm, OrderStatusForm, AdminForm
from django.db.models import Sum
from account.decorators import admin_login_required
from django.http import JsonResponse

from products.models import Product
from category.models import Category
from orders.models import Order
from offers.models import Coupon
from account.models import CustomUser

import datetime
from datetime import timedelta


# Create your views here.

@admin_login_required
def homeView(request):

    # ===========chart data by ajax request======
    if request.method == 'POST':
        order_success = Order.objects.filter(status = 'success').count()
        order_shipped = Order.objects.filter(status = 'shipped').count()
        order_deliverd = Order.objects.filter(status = 'deliverd').count()
        order_cancelled = Order.objects.filter(status = 'cancelled').count()

    # ========mothly product sale=========

        date_today = datetime.date.today()

        last_one_month = date_today - timedelta(days=30)
        second_last_month = last_one_month - timedelta(days=30)
        third_last_month = second_last_month - timedelta(days=30)
        fourth_last_month = third_last_month - timedelta(days=30)
        fifth_last_month = fourth_last_month - timedelta(days=30)
        sixth_last_month = fifth_last_month - timedelta(days=30)

        product_sale_1 = Order.objects.filter(updated_at__range=[last_one_month, date_today], status = 'deliverd').aggregate(last_one_month = Sum('total_amount'))
        product_sale_2 = Order.objects.filter(updated_at__range=[second_last_month, last_one_month], status = 'deliverd').aggregate(second_last_month = Sum('total_amount'))
        product_sale_3 = Order.objects.filter(updated_at__range=[third_last_month, second_last_month], status = 'deliverd').aggregate(third_last_month = Sum('total_amount'))
        product_sale_4 = Order.objects.filter(updated_at__range=[fourth_last_month, third_last_month], status = 'deliverd').aggregate(fourth_last_month = Sum('total_amount'))
        product_sale_5 = Order.objects.filter(updated_at__range=[fifth_last_month, fourth_last_month], status = 'deliverd').aggregate(fifth_last_month = Sum('total_amount'))
        product_sale_6 = Order.objects.filter(updated_at__range=[sixth_last_month, fifth_last_month], status = 'deliverd').aggregate(sixth_last_month = Sum('total_amount'))

        last_month_sale = product_sale_1.get('last_one_month')
        second_last_month_sale = product_sale_2.get('second_last_month')
        third_last_month_sale = product_sale_3.get('third_last_month')
        fourth_last_month_sale = product_sale_4.get('fourth_last_month')
        fifth_last_month_sale = product_sale_5.get('fifth_last_month')
        sixth_last_month_sale = product_sale_6.get('sixth_last_month')
        order_status = [order_success, order_shipped, order_deliverd, order_cancelled]
        monthly_sale = [
            sixth_last_month_sale,
            fifth_last_month_sale,
            fourth_last_month_sale,
            third_last_month_sale,
            second_last_month_sale,
            last_month_sale,
        ]





        chart_data = { 
            'order_status' : order_status,
            'monthly_sale' : monthly_sale
                }
        return JsonResponse(chart_data , safe=False)

    # ============total quantity of remaining products============
    # r_qty = Product.objects.aggregate(total_product_qty = Sum('qty'))

    # ============total quantity of deliverd products============
    # o_qty = Order.objects.aggregate(total_product_qty = Sum('qty'))



    # ============total revenue============
    products = Product.objects.all()
    total_revenue = 0
    for product in products:
        selling_price = product.selling_price
        qty = product.qty
        total = selling_price*qty
        total_revenue+=total

    # ============total cost============
    products = Product.objects.all()
    total_cost = 0
    for product in products:
        cost_price = product.cost_price
        qty = product.qty
        total = cost_price*qty
        total_cost+=total

    try:
    # ============total sales==========
        total_amount = Order.objects.filter(status = 'deliverd').aggregate(total_sale = Sum('total_amount'))
        total_sale = total_amount.get('total_sale')

        # ========total cost of saled product=====
        total_sale_cost = Order.objects.filter(status = 'deliverd').aggregate(total_saled_cost = Sum('total_cost'))
        total_saled_cost = total_sale_cost.get('total_saled_cost')

        # ===========total profit=========
        total_profit = total_sale-total_saled_cost


    except:
            # ============total sales==========
        total_amount = 0
        total_sale = 0

        # ========total cost of saled product=====
        total_sale_cost = 0
        total_saled_cost = 0

        # ===========maximum profit=========
        total_profit = 0


    # ===========maximum profit=========
    maximum_profit = total_revenue-total_cost


    context = {
        'total_revenue' : total_revenue,
        'total_cost' : total_cost,
        'maximum_profit' : maximum_profit,
        'total_sale' : total_sale,
        'total_saled_cost' : total_saled_cost,
        'total_profit' : total_profit,

    }

    return render(request, 'super_admin/home.html',context)


    


@method_decorator(admin_login_required, name='dispatch')
class CategoryAddView(View):
    def get(self, request):
        form = CategoryDetailsForm()
        context = {'form' : form}
        return render(request, 'super_admin/category_add.html', context)
    def post(self, request):
        form = CategoryDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            prod_name = form.cleaned_data.get('name')
            print('=========', prod_name)
            try:
                same_prod = Category.objects.get(name__iexact = prod_name)
                print('=========', same_prod)
                messages.info(request, 'Category with same name already exist!')
                context = {'form' : form}
                return render(request, 'super_admin/category_add.html', context)                
            except:
                form.save()
                messages.success(request, 'New category added successfuly')
                return redirect('super_admin:category_add')
        messages.error(request, 'Form is not valid')
        return redirect('super_admin:category_add')

@admin_login_required
def categoryListView(request):
    categorys = Category.objects.all()
    context = {'categorys' : categorys}
    return render(request, 'super_admin/category_list.html', context )

@admin_login_required
def categoryDetailsView(request, pk):
    category = Category.objects.get(id=pk)
    context = {'category' : category}
    return render(request, 'super_admin/category_details.html', context)

@method_decorator(admin_login_required, name='dispatch')
class CategoryEditView(View):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        form = CategoryDetailsForm(instance=category)
        context = {'form' : form}
        return render(request, 'super_admin/category_add.html', context)
    def post(self, request, pk):
        category = Category.objects.get(id=pk)
        form = CategoryDetailsForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category edited successfuly')
            return redirect('super_admin:category_list')
        messages.error(request, 'Form is not valid')
        return redirect('super_admin:category_add')

@method_decorator(admin_login_required, name='dispatch')
def categoryDeleteView(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    messages.info(request, 'Category deleted!')
    return redirect('super_admin:category_list')









@method_decorator(admin_login_required, name='dispatch')
class ProductAddView(View):
    def get(self, request):
        form = ProductDetailsForm()
        context = {'form' : form}
        return render(request, 'super_admin/product_add.html', context)
    def post(self, request):
        form = ProductDetailsForm(request.POST, request.FILES)
        context = {'form' : form}
        if form.is_valid():
            form.save()
            messages.success(request, 'New product added successfuly')
            return redirect('super_admin:product_add')
        messages.error(request, 'Form is not valid')
        return render(request, 'super_admin/product_add.html', context)

@admin_login_required
def productListView(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'super_admin/product_list.html', context )

@admin_login_required
def productDetailsView(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product' : product}
    return render(request, 'super_admin/product_details.html', context)

@method_decorator(admin_login_required, name='dispatch')
class ProductEditView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        form = ProductDetailsForm(instance=product)
        context = {'form' : form}
        return render(request, 'super_admin/product_add.html', context)
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        form = ProductDetailsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product edited successfuly')
            return redirect('super_admin:product_list')
        messages.error(request, 'Form is not valid')
        return redirect('super_admin:product_add')

@admin_login_required
def productDeleteView(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    messages.info(request, 'Product deleted!')
    return redirect('super_admin:product_list')

@admin_login_required
def couponListView(request):
    coupons = Coupon.objects.all()
    context = {"coupons": coupons}
    return render(request, "super_admin/coupon_list.html", context)

@admin_login_required
def couponAddView(request):
    form = CouponForm

    if request.method == "POST":
        form = CouponForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Coupon Added Successfully.")
            return redirect("super_admin:coupon_add")

    context = {"form": form}
    return render(request, "super_admin/coupon_add.html", context)

@method_decorator(admin_login_required, name='dispatch')
class CouponEditView(View):
    def get(self, request, pk):
        coupon = Coupon.objects.get(id=pk)
        form = CouponForm(instance=coupon)
        context = {'form' : form}
        return render(request, 'super_admin/coupon_add.html', context)
    def post(self, request, pk):
        coupon = Coupon.objects.get(id=pk)
        form = CouponForm(request.POST, instance=coupon)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coupon edited successfuly')
            return redirect('super_admin:coupon_list')
        messages.error(request, 'Form is not valid')
        return redirect('super_admin:coupon_add')

@admin_login_required
def couponDeleteView(request, pk):
    Coupon.objects.get(id=pk).delete()
    messages.info(request, 'Coupon deleted!')
    return redirect("super_admin:coupon_list")

@method_decorator(admin_login_required, name='dispatch')
class OrderListView(View):
    def get(self, request):
        orders = Order.objects.all().order_by('-id')
        form = OrderStatusForm
        context = {'orders' : orders, 'form' : form}
        return render(request, 'super_admin/order_list.html', context )
    def post(self, request):
        order_id = request.POST.get('order_id')
        order_status = request.POST.get('status')
        order = Order.objects.get(id = order_id)
        order.status = order_status
        order.save()
        messages.success(request, 'Order Status changed successfuly')
        return redirect('super_admin:order_list')


def customerListView(request):
    user = CustomUser.objects.filter(is_admin = False, is_superadmin = False).order_by('-id')
    context = {'user' : user}
    return render(request, 'super_admin/user_list.html', context )

def adminListView(request):
    user = CustomUser.objects.filter(is_admin = True).order_by('-id')
    context = {'user' : user}
    return render(request, 'super_admin/user_list.html', context )

@method_decorator(admin_login_required, name='dispatch')
class AdminRequestListView(View):
    def get(self, request):
        admin = CustomUser.objects.filter(is_admin = False, is_superadmin = False, is_admin_request = True).order_by('-id')
        form = AdminForm
        context = {'admin' : admin, 'form' : form}
        return render(request, 'super_admin/admin_request_list.html', context )
    def post(self, request):
        admin_id = request.POST.get('admin_id')
        admin = CustomUser.objects.get(id=admin_id ,is_admin = False, is_superadmin = False, is_admin_request = True)
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admin requested accepted')
            return redirect('super_admin:admin_request_list')
        messages.error(request, 'Form is not valid')
        return redirect('super_admin:admin_request_list')
