from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product ,Brand,Review
from django.db.models.aggregates import Avg
from .serializers import productlistserializers ,brandlistserializers,branddetailserializers,productdetailserializers,reviewserializers
from rest_framework import generics

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

class productdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class= productdetailserializers


class brandlistapi(generics.ListCreateAPIView):
    queryset=Brand.objects.all()
    serializer_class= brandlistserializers

class branddetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Brand.objects.all()
    serializer_class= branddetailserializers


