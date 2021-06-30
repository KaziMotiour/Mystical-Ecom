from django.contrib import admin
from .models import Voucher, AddToCart, PlaceOrder, OrderdItem

# Register your models here.
admin.site.register(Voucher)
admin.site.register(AddToCart)
admin.site.register(PlaceOrder)
admin.site.register(OrderdItem)
