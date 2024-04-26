from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100,default="Seller Name")
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="../shop/static/shop/default.png")   #pip install pillow
    condn = models.CharField(max_length=50,default="")
    seller_name = models.CharField(max_length=100)
    mobno=models.IntegerField()
    email=models.EmailField(default="@gmail.com",max_length=100)
    curr_year= models.IntegerField(default="1")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    #contact_id=models.AutoField
    name= models.CharField(max_length=100)
    mobno=models.IntegerField()
    email=models.EmailField(default="@gmail.com",max_length=100)
    curr_year= models.IntegerField()
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name

    