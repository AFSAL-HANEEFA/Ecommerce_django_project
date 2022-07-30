from django.urls import path
from super_admin import views

app_name = 'super_admin'
urlpatterns = [
    path('',views.homeView, name='home'),
    path('chart/',views.homeView, name='home'),

    path('category-add',views.CategoryAddView.as_view(), name='category_add'),
    path('category-list/', views.categoryListView, name= 'category_list'),
    path('category-details/<str:pk>', views.categoryDetailsView, name= 'category_details'),
    path('category-edit/<str:pk>', views.CategoryEditView.as_view(), name= 'category_edit'),
    path('category-delete/<str:pk>', views.categoryDeleteView, name= 'category_delete'),

    path('product-add',views.ProductAddView.as_view(), name='product_add'),
    path('product-list/', views.productListView, name= 'product_list'),
    path('product-details/<str:pk>', views.productDetailsView, name= 'product_details'),
    path('product-edit/<str:pk>', views.ProductEditView.as_view(), name= 'product_edit'),
    path('product-delete/<str:pk>', views.productDeleteView, name= 'product_delete'),

    path('coupon-add',views.couponAddView, name='coupon_add'),
    path('coupon-list/', views.couponListView, name= 'coupon_list'),
    path('coupon-edit/<str:pk>', views.CouponEditView.as_view(), name= 'coupon_edit'),
    path('coupon-delete/<str:pk>', views.couponDeleteView, name= 'coupon_delete'),

    path('order-list/', views.OrderListView.as_view(), name= 'order_list'),

    path('customer-list/', views.customerListView, name= 'customer_list'),
    path('admin-list/', views.adminListView, name= 'admin_list'),
    path('admin-request-list/', views.AdminRequestListView.as_view(), name= 'admin_request_list'),


]



