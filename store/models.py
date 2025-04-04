from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    image = CloudinaryField('image', blank=True, null=True )
    quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse("product-page", kwargs= {"id":self.id} )

    def __str__(self):
        return  self.product_name

