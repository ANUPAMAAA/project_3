from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=True)
    mobile=models.IntegerField(null=True)
    uname=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=15,null=True)
class Country(models.Model):
    cname=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=10,null=True)
class Brand(models.Model):
    bimage=models.ImageField(upload_to='media',null=True)
    brand_name=models.CharField(max_length=50,null=True)
    brand_status=models.CharField(max_length=10,null=True)
class Category(models.Model):
    cimage = models.ImageField(upload_to='media', null=True)
    category_name=models.CharField(max_length=50,null=True)
    category_status=models.CharField(max_length=70,null=True)
class Product(models.Model):
    p_image = models.ImageField(upload_to='media', null=True)
    p_code = models.IntegerField(null=True)
    p_name = models.CharField(max_length=50,null=True)
    p_price = models.IntegerField(null=True)
    total_amo = models.IntegerField(null=True)
    p_brand = models.CharField(max_length=45,null=True)
    p_category = models.CharField(max_length=35,null=True)
    p_date = models.DateField(null=True)
    up_date =models.DateField(null=True)
    op_stock = models.IntegerField(null=True)
    cp_stock = models.IntegerField(null=True)
    p_status = models.CharField(max_length=45,null=True)
class Cart(models.Model):
    user = models.ForeignKey(Signup, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phn_no = models.CharField(max_length=20)
    email = models.EmailField()
    payment_method = models.CharField(max_length=20)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    products = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, null=True, default='pending')
class Deliveryp(models.Model):
    dp_id = models.IntegerField(null=True)
    dp_pic = models.ImageField(upload_to='media',null=True)
    dp_name = models.CharField(max_length=30,null=True)
    dp_email = models.EmailField()
    dp_number = models.IntegerField(null=True)
    dp_uname = models.CharField(max_length=10,null=True)
    dp_password = models.CharField(max_length=10,null=True)
    dp_date = models.DateField(null=True)
class Oder_notification(models.Model):
    dp_name = models.ForeignKey(Deliveryp,on_delete=models.CASCADE,null=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, null=True)
class Enquiry(models.Model):
    e_name= models.CharField(max_length=20,null=True)
    e_email = models.EmailField()
    e_phone = models.IntegerField(null=True)
    e_question = models.TextField(null=True)




