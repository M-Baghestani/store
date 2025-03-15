from django.urls import path, include
from .views import helloworld
from .views import (
    CategoryListCreateView, CategoryDetailView,
    CustomerListCreateView, CustomerDetailView,
    ProductListCreateView, ProductDetailView,
    OrderListCreateView, OrderDetailView
) 

urlpatterns = [
    path('',helloworld),

    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
