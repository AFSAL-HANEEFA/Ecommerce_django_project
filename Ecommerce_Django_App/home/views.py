from django.shortcuts import render
from category.models import Category
from products.models import Product


def homeView(request):
    categories = Category.objects.all().order_by('order_by')
    products_in_home = Product.objects.filter(is_visible_home_img = True).order_by('home_img_order')

    context = {
    'categories' : categories,
    'products_in_home' : products_in_home
    }
    return render(request, 'user/home.html', context)

