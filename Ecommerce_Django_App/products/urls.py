from django.urls import path
from products import views
app_name = 'products'

urlpatterns = [
    path('product-list/<str:pk>/', views.productListView, name = 'product_list'),
    path('product-details/<str:pk>/', views.productDetailsView, name = 'product_details'),
]
