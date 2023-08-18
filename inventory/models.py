from django.db import models
from vendor.models import Vendor
class Product(models.Model):
    Vendor=models.ForeignKey(Vendor,null=True,on_delete=models.CASCADE)
    #   one vendor can have many customers     
    name=models.CharField(max_length=32, null=True)
    price =models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField(max_length=255)
    image =models.ImageField(upload_to='images')
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated =models.DateTimeField(auto_now=True)
    stock=models.PositiveIntegerField()

