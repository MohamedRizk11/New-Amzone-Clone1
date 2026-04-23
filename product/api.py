from warnings import filters
from .myfilter import myfilter
from .mypagination import mypagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend 
from .models import Product ,Brand,Review
from django.db.models.aggregates import Avg
from .serializers import productlistserializers ,brandlistserializers,branddetailserializers,productdetailserializers,reviewserializers
from rest_framework import generics, filters


'''@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    data = productlistserializers(products,many=True,context={'request':request}).data
    return Response({'products':data})


@api_view(['GET'])
def product_detail_api(request,product_id):
    products = Product.objects.get(id=product_id)
    data = productlistserializers(products,context={'request':request}).data
    return Response({'product':data})
'''

class productlistapi(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class= productlistserializers
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['brand', 'price']
    search_fields = ['name', 'subtitels', 'desciptions']
    ordering_fields = ['price', 'sku']
    filterset_class= myfilter
    pagination_class = mypagination
class productdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class= productdetailserializers


class brandlistapi(generics.ListCreateAPIView):
    queryset=Brand.objects.all()
    serializer_class= brandlistserializers

class branddetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Brand.objects.all()
    serializer_class= branddetailserializers


