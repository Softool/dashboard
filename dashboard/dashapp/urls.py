from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='Home'),
    path('customer/<str:pk_test>/', views.customer, name='Customer'),
    path('product', views.product, name='Product'),
    path('create_order/',views.createOrder, name='Create_order'),
    path('create_customer/', views.createCustomer, name='Create_customer'),
    path('update_order/<str:pk>/', views.updateOrder, name='Update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='Delete_order'),

]