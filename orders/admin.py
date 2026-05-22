from django.contrib import admin


from .models import order,orderdetail,coupon,Cart,Cartdetail


admin.site.register(order)
admin.site.register(orderdetail)
admin.site.register(coupon)
admin.site.register(Cart)
admin.site.register(Cartdetail)
