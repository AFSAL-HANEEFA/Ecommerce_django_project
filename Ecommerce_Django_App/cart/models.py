from django.db import models
from account.models import CustomUser
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='u_cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE )
    qty = models.PositiveIntegerField(default=1 )

    def __str__(self):

        return self.product.name

    def totalPrice(self):
        total_price = self.product.selling_price * self.qty
        return int(total_price)
