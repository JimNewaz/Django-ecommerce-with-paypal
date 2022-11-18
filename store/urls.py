
from django.urls import path, include
from . import views

urlpatterns = [    
    path('', views.store, name="store"), 
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="updateItem"),
    path('process-order/', views.processOrder, name="process-order")
]
