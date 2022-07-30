from django.db import models

STATUS_CHOICES = (
    ('success', 'success'),
    ('shipped', 'shipped'),
    ('out of selivery', 'out of delivery'),
    ('deliverd', 'deliverd'),
    ('cancelled', 'cancelled'),
)
class Order(models.Model):
    user = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    product = models.CharField(max_length=100)
    product_id = models.PositiveIntegerField()
    product_selling_price = models.FloatField()
    qty = models.PositiveIntegerField()
    total_amount = models.FloatField(null=True)
    total_cost = models.FloatField(default=0)
    image = models.ImageField(upload_to = 'order_image')
    coupon = models.PositiveIntegerField(null=True, blank=True)
    payment = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    tracking_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product

