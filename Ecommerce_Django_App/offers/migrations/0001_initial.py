# Generated by Django 4.0.5 on 2022-07-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(max_length=50)),
                ('coupon_code', models.CharField(max_length=50, unique=True)),
                ('discount', models.PositiveIntegerField(help_text='Offer in Rupees', null=True)),
                ('is_redeemed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
