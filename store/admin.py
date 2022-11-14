from django.contrib import admin

#user: jim
#pass: 123456

# Register your models here.
from .models import * 

admin.site.register(Customer)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(OrderItem)

admin.site.register(ShippingAddress)