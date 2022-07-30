from django.db import models
from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    marking_price = models.FloatField()
    selling_price = models.FloatField()
    cost_price = models.FloatField(default=0)
    qty = models.IntegerField(default=1)
    screen_size = models.CharField(max_length=100,blank=True, null=True)
    os = models.CharField(max_length=100,blank=True, null=True)
    processor = models.CharField(max_length=100,blank=True, null=True)
    camera = models.CharField(max_length=100, blank=True, null=True)
    RAM = models.CharField(max_length=5,blank=True, null=True)
    ROM = models.CharField(max_length=6,blank=True, null=True)
    color = models.CharField(max_length=50,blank=True, null=True)
    warranty = models.CharField(max_length=100, default='1 Year',null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to = 'product_images')
    spec1 = models.CharField(max_length=200, null=True, blank=True)
    spec2 = models.CharField(max_length=200, null=True, blank=True)
    spec3 = models.CharField(max_length=200, null=True, blank=True)
    spec4 = models.CharField(max_length=200, null=True, blank=True)
    spec5 = models.CharField(max_length=200, null=True, blank=True)
    spec6 = models.CharField(max_length=200, null=True, blank=True)
    spec7 = models.CharField(max_length=200, null=True, blank=True)
    spec8 = models.CharField(max_length=200, null=True, blank=True)
    spec9 = models.CharField(max_length=200, null=True, blank=True)
    spec10 = models.CharField(max_length=200, null=True, blank=True)
    spec11 = models.CharField(max_length=200, null=True, blank=True)
    spec12 = models.CharField(max_length=200, null=True, blank=True)
    spec13 = models.CharField(max_length=200, null=True, blank=True)
    spec14 = models.CharField(max_length=200, null=True, blank=True)
    spec15 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True, help_text='default-active')
    order_by = models.PositiveIntegerField(blank=True, null=True)
    trending = models.BooleanField(default=False,help_text='default-not trending')
    offer = models.BooleanField(default=False,help_text='default-no offer')
    banner_img = models.ImageField(upload_to = 'banner', null= True, blank=True)
    banner_img_order = models.PositiveIntegerField(blank=True, null=True, help_text='Order in which product shows in carousel')
    is_visible_banner = models.BooleanField(default=True,help_text='default-show in carousel')
    home_img = models.ImageField(upload_to = 'home_product', null= True, blank=True)
    home_img_order = models.PositiveIntegerField(blank=True, null=True, help_text='Order in which product shows in home page')
    is_visible_home_img = models.BooleanField(default=True,help_text='default-show in home')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def discount(self):
        discount = round((self.marking_price - self.selling_price) * (100/self.marking_price),1)
        return discount


