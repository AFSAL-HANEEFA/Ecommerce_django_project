from django.db import models

class Category(models.Model):

    CATEGORY_CHOICE = (
    ('mac', 'mac'),
    ('ipad', 'ipad'),
    ('iphone', 'iphone'),
    ('watch', 'watch'),
    ('airpods', 'airpods'),
    ('homepod', 'homepod')
)

    category = models.CharField(choices=CATEGORY_CHOICE,max_length=100)
    image = models.ImageField(upload_to = 'category_images')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, help_text='0-hidden, 1-default')
    trending = models.BooleanField(default=False,help_text='0-default, 1-trending')
    offfer = models.BooleanField(default=False,help_text='0-default, 1-offer')
    order_by = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return(self.category)