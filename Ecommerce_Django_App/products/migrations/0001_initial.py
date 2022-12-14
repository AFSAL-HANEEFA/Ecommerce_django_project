# Generated by Django 4.0.5 on 2022-07-10 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('tag', models.CharField(blank=True, max_length=50, null=True)),
                ('marking_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('cost_price', models.FloatField(default=0)),
                ('qty', models.IntegerField(default=1)),
                ('screen_size', models.CharField(blank=True, max_length=100, null=True)),
                ('os', models.CharField(blank=True, max_length=100, null=True)),
                ('processor', models.CharField(blank=True, max_length=100, null=True)),
                ('camera', models.CharField(blank=True, max_length=100, null=True)),
                ('RAM', models.CharField(blank=True, max_length=5, null=True)),
                ('ROM', models.CharField(blank=True, max_length=6, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('warranty', models.CharField(blank=True, default='1 Year', max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(upload_to='product_images')),
                ('spec1', models.CharField(blank=True, max_length=200, null=True)),
                ('spec2', models.CharField(blank=True, max_length=200, null=True)),
                ('spec3', models.CharField(blank=True, max_length=200, null=True)),
                ('spec4', models.CharField(blank=True, max_length=200, null=True)),
                ('spec5', models.CharField(blank=True, max_length=200, null=True)),
                ('spec6', models.CharField(blank=True, max_length=200, null=True)),
                ('spec7', models.CharField(blank=True, max_length=200, null=True)),
                ('spec8', models.CharField(blank=True, max_length=200, null=True)),
                ('spec9', models.CharField(blank=True, max_length=200, null=True)),
                ('spec10', models.CharField(blank=True, max_length=200, null=True)),
                ('spec11', models.CharField(blank=True, max_length=200, null=True)),
                ('spec12', models.CharField(blank=True, max_length=200, null=True)),
                ('spec13', models.CharField(blank=True, max_length=200, null=True)),
                ('spec14', models.CharField(blank=True, max_length=200, null=True)),
                ('spec15', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(default=True, help_text='default-active')),
                ('order_by', models.PositiveIntegerField(blank=True, null=True)),
                ('trending', models.BooleanField(default=False, help_text='default-not trending')),
                ('offer', models.BooleanField(default=False, help_text='default-no offer')),
                ('banner_img', models.ImageField(blank=True, null=True, upload_to='banner')),
                ('banner_img_order', models.PositiveIntegerField(blank=True, help_text='Order in which product shows in carousel', null=True)),
                ('is_visible_banner', models.BooleanField(default=True, help_text='default-show in carousel')),
                ('home_img', models.ImageField(blank=True, null=True, upload_to='home_product')),
                ('home_img_order', models.PositiveIntegerField(blank=True, help_text='Order in which product shows in home page', null=True)),
                ('is_visible_home_img', models.BooleanField(default=True, help_text='default-show in home')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
