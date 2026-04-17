from django.db import models

class company(models.Model):
    logo =models.ImageField(upload_to='company_logo')
    description = models.TextField(max_length=40000)
    name= models.CharField(max_length=30)
    facebook_link=models.URLField(max_length=200,null=True,blank=True)
    twitter_link=models.URLField(max_length=200,null=True,blank=True)
    linkedin_link=models.URLField(max_length=200,null=True,blank=True)
    instagram_link=models.URLField(max_length=200,null=True,blank=True)
    threds_link=models.URLField(max_length=200,null=True,blank=True)
    email=models.TextField(max_length=200,null=True,blank=True)
    phone=models.TextField(max_length=200,null=True,blank=True)
    address=models.TextField(max_length=200,null=True,blank=True)
    androidapp_link=models.URLField(max_length=200,null=True,blank=True)
    iosapp_link=models.URLField(max_length=200,null=True,blank=True)
    call_us= models.CharField(max_length=30)
    email_us= models.CharField(max_length=30)


    def __str__(self):
        return self.name