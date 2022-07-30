from django import forms
from category.models import Category
from products.models import Product
from offers.models import Coupon
from orders.models import Order
from account.models import CustomUser



class CategoryDetailsForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']


class AdminForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['is_admin']

        # widgets = { 
        #     'is_admin' : forms.CheckboxInput(attrs={'class' : 'form-control'})
        # }