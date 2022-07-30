from django.urls import path
from. import views
app_name = 'offers'

urlpatterns = [
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),
    path('remove-coupon/', views.remove_coupon, name='remove_coupon'),
]
