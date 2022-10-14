from django.urls import path,include

from account.models import product
from . import views
urlpatterns = [
  path('',views.home, name='home'),
  path('product/',views.product, name='product'),
  path('customer/<str:pk_test>', views.customer, name='customer'),
  path('Create_Order/<str:pk>/',views.CreateOrder, name='Create_Order'),
  path('UpdateOrder/<str:pk>',views.UpdateOrder, name='UpdateOrder'),
  path('DeleteOrder/<str:pk>',views.DeleteOrder, name='DeleteOrder'),
]


    