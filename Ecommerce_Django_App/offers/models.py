from django.db import models
from account.models import CustomUser

class Coupon(models.Model):
    coupon_name = models.CharField(max_length=50)
    coupon_code = models.CharField(max_length=50, unique=True)
    discount = models.PositiveIntegerField(help_text="Offer in Rupees", null=True)
    is_redeemed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.coupon_name
