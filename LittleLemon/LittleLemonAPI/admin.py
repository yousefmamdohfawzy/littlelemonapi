from django.contrib import admin
from .models import MenuItem ,OrderItem,Order,Cart,Category

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
