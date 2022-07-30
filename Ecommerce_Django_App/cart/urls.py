from django.urls import path
from cart import views
app_name = 'cart'
urlpatterns = [
    
    path('', views.cartView, name = 'cart'),

    path('add-to-cart/', views.addToCartView, name= 'add_to_cart'),
    path('add-to-cart/<str:pk>/', views.addToCartBeforeLoginView, name= 'add_to_cart_brfore_login'),
    path('change-qty/', views.changeQtyView, name  = 'change_qty'),

]
