from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Brand , Productimages , Review
from django.db.models.aggregates import Max, Count

# Create your views here.


class Productlist(ListView):
    model = Product
    paginate_by = 20


class Producdetail(DetailView):
    model = Product    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"]= Product.objects.filter(brand=self.get_object().brand)
        return context

class Brandlist(ListView):
    model=Brand
    queryset=Brand.objects.annotate(products_count=Count('product_brand'))
    
class Branddetail(ListView):
    model=Product
    template_name = 'product/brand_detail.html'
    paginate_by= 20 

    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(products_count=Count('product_brand'))[0]
        return context
    