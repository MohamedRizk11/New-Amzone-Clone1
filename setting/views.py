from django.shortcuts import render
from django.db.models import Count
from product.models import Product,Brand,Review


# Create your views here.
def Home(request):
    brands=Brand.objects.all().annotate(product_count=Count('product_brand'))
    sale_products= Product.objects.filter(falg='Sale')[:10]
    featured_products= Product.objects.filter(falg='Feature')[:6]
    new_products= Product.objects.filter(falg='New')[:10]
    reviews= Review.objects.all()[:5]



    return render (request,'settings/Home.html',{
        'brands':brands,
        'sale_products':sale_products,
        'featured_products':featured_products,
        'new_products':new_products,
        'reviews':reviews,



        })