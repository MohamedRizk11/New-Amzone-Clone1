from django_filters import rest_framework as  filters 
from .models import Product

class myfilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['brand', 'price']
    price_min = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="price", lookup_expr='lte')