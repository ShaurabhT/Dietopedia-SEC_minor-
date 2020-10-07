from django.db import models

# Create your models here.
class Customers(models.Model):
    First_Name= models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=10)
    Age=models.IntegerField()
    Email= models.EmailField(max_length=70,blank=True, null= True, unique= True)
