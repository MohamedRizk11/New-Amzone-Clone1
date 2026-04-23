from rest_framework import serializers
from .models import Product ,Brand,Review
from django.db.models.aggregates import Avg
from taggit.serializers import TagListSerializerField,TaggitSerializer



class productlistserializers(serializers.ModelSerializer):
   # brand=brandlistserializers() 
    brand=serializers.StringRelatedField() 
    avg_rate=serializers.SerializerMethodField()
    reviews_count=serializers.SerializerMethodField()
    
    
    class Meta:
        model=Product
        fields= '__all__'
    def get_avg_rate(self,product):
        avg = product.reiew_product.aggregate(rate_avg=Avg('rate')) 
        if not avg['rate_avg']:
            result =0 
            return result
        return avg['rate_avg']
    def get_reviews_count(self,product:Product):
        reviews=product.reiew_product.all().count()
        return reviews
    
class reviewserializers(serializers.ModelSerializer):
    class Meta:
       model=  Review
       fields= '__all__'

class productdetailserializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField() 
    avg_rate=serializers.SerializerMethodField()
    reviews_count=serializers.SerializerMethodField()
    reviews = reviewserializers(source='reiew_product',many=True)
    tags = TagListSerializerField()
    class Meta:
        model=Product
        fields= '__all__'

    def get_avg_rate(self,product):
        avg = product.reiew_product.aggregate(rate_avg=Avg('rate')) 
        if not avg['rate_avg']:
            result =0 
            return result
        return avg['rate_avg']
    def get_reviews_count(self,product:Product):
        reviews=product.reiew_product.all().count()
        return reviews               


class brandlistserializers(serializers.ModelSerializer):

    class Meta:
        model=Brand
        fields= '__all__'
class branddetailserializers(serializers.ModelSerializer):
    products = productlistserializers(source='product_brand',many=True)

    
    class Meta:
        model=Brand
        fields= '__all__' 