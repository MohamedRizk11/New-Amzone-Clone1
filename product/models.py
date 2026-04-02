from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.utils.text import slugify 
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

FLag_types=(
('Sale','Sale'),
('New','New'),
('Feature','Feature')
)
# Create your models here.
class Product (models.Model):
    name = models.CharField(_('Name'),max_length=120)
    falg = models.CharField(_('Flag'),max_length=20,choices=FLag_types)
    image= models.ImageField(_('Image'), upload_to='products')
    price= models.FloatField(_('Price'),)
    sku = models.CharField(_('Sku'),max_length=20)
    subtitels=models.CharField(_('Subtiltle'),max_length=300)
    desciptions= models.TextField(_('Descriptions'),max_length=40000)
    quantity= models.IntegerField(_('Quantity'),)
    brand=models.ForeignKey('Brand',verbose_name=_('Brand'), related_name='product_brand', on_delete=models.SET_NULL,null=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Product, self).save(*args, **kwargs) # Call the real save() method
    
class Productimages (models.Model):
    product=models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_image',on_delete=models.CASCADE)
    image= models.ImageField(_('Image'),upload_to='product_images')

    def __str__(self):
        return str(self.product)
    


class Brand (models.Model):
    name = models.CharField(_('Name'),max_length=120)
    image= models.ImageField( _('Image'),upload_to='brand')
    def __str__(self):
        return self.name
    


class Review (models.Model):
    user= models.ForeignKey(User,verbose_name=_('User'), related_name='reiew_auther', on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,verbose_name=_('Product'), related_name='reiew_product', on_delete=models.CASCADE)
    rate=models.IntegerField(_('Rate'),)
    rewiew=models.CharField(_('Review'),max_length=300)
    create_at=models.DateTimeField(_('Create_at'),default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.product}"
    