from django.contrib import admin

# Register your models here.
from .models import Product , Brand , Productimages , Review



class ProductImageTabular(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Productimages


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','quantity','price','falg']
    search_fields=['name','price','subtitle']
    list_filter=['name','price']
    inlines = [ProductImageTabular]

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Productimages)
admin.site.register(Review)