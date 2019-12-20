from django.db import models

# Create your models here.
class ResiterModel(models.Model):
 id=models.AutoField(primary_key=True)
 name=models.CharField(max_length=30)
 contact=models.IntegerField()
 emailid=models.EmailField(default=False)
 password=models.CharField(max_length=30)
 status=models.CharField(max_length=30)
 doj=models.DateField(auto_now_add=True)

class ProductModel(models.Model):
 pid=models.IntegerField(primary_key=True,default=False)
 pname=models.CharField(max_length=30)
 bprice=models.FloatField(default=False)
 pqnty=models.IntegerField()
 pinfo=models.TextField()
 images=models.ImageField(upload_to="product/")
 status=models.CharField(max_length=30)
 uid=models.ForeignKey(ResiterModel,on_delete=models.CASCADE)
