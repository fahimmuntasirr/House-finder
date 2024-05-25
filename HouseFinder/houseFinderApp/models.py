from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product_pic = models.ImageField(upload_to="product_image", null=True, blank=True )
    product_contact = models.IntegerField(null=True, blank=True)
    product_address = models.CharField(max_length=100,null=True, blank=True)
    product_description = models.CharField(max_length=500, null=True, blank=True)
    product_price = models.IntegerField(null=True, blank=True)
    product_title = models.CharField(max_length=500, null=True, blank=True)
    require = models.CharField(max_length=100,null=True, blank=True)
    if_posted = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=100,null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    dp = models.ImageField(upload_to="dp_image", null=True, blank=True )

    def __str__(self):
        return str(self.user)
 