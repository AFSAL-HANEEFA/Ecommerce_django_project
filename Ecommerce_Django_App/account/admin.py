from django.contrib import admin
from account.models import CustomUser, UserMobile

admin.site.register(CustomUser)
admin.site.register(UserMobile)
