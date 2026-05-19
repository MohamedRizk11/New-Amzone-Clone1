from django.db import models
from django.contrib.auth.models import User
from utils.genarate_code import genarate_code
from django.utils import timezone 
from datetime import timedelta , datetime
from product.models import Product

Status_cart=(('Inprogress','Inprogress'),
             ('Completed','Completed')
             )

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=30 ,choices=Status_cart)

class Cartdetail(models.Model):
    cart= models.ForeignKey(Cart,related_name='cart_detail', on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField()
    total=models.FloatField(null=True,blank=True)


Status_order=(('Recieved','Recieved'),
             ('Progressed','Progressed'),
             ('Shipped','Shipped'),
             ('Delivered','Delivered'),
             )    

class order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=30 ,choices=Status_order)    
    code= models.CharField(default=genarate_code())
    order_time= models.DateTimeField(default=timezone.now)
    deliver_time= models.DateTimeField(null=True,blank=True)


class orderdetail(models.Model):
    cart= models.ForeignKey(Cart,related_name='order_detail', on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    price=models.FloatField()
    quantity=models.IntegerField()
    total=models.FloatField(null=True,blank=True)



class coupon(models.Model):
    code=models.CharField(max_length=20)
    discount=models.IntegerField()
    quantity=models.IntegerField()
    start_date=models.DateField(default=timezone.now)    
    end_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
       week = timedelta(days=7)
       self.end_date=self.start_date + week
       super(coupon, self).save(*args, **kwargs) # Call the real save() method    
