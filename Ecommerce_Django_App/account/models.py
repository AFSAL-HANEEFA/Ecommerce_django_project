from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from cropperjs.models import CropperImageField

# ================= custom user model ===============

class CustomBaseUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, mobile, password= None ):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")

        user = self.model(
            first_name =first_name,
            last_name =last_name,
            username = username,
            email = self.normalize_email(email),
            mobile = mobile
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(
        self, username, email, password, mobile, first_name='', last_name= ''
    ):
        user = self.create_user(
            first_name =first_name,
            last_name =last_name,
            username = username,
            email = self.normalize_email(email),
            mobile = mobile,
            password= password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_verified = True
        user.save(using=self._db)
        return user




class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=55,null=True, blank=True)
    last_name = models.CharField(max_length=55,null=True, blank=True)
    username  =models.CharField(max_length=55, unique=True)
    email = models.EmailField(max_length=55, unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_admin_request = models.BooleanField(default=False)

    GENDER_CHOICES = (
        ('male' , 'Male'),
        ('female' , 'Female'),
        ('other' , 'Other')

    )
    profile_pic = models.ImageField(upload_to = 'user_pro_pic', default='default/pro_pic.png')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['username', 'email' ]

    objects = CustomBaseUserManager()

    def __str__(self):
        return self.username

    def full_name(self):
        return f"{self.first_name} {self.last_name}"   
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    def cart_number(self):
        no_of_cart_items = self.u_cart.count()
        return no_of_cart_items

class UserMobile(models.Model):
    mobile = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.mobile