from django.db import models

# Create your models here.
class Query(models.Model):
    name=models.CharField(max_length=60,blank=True, null=True)
    email=models.CharField(max_length=200,blank=True, null=True)
    countrycode=models.CharField(max_length=10,blank=True, null=True)
    phone=models.CharField(max_length=50,blank=True, null=True)
    message=models.TextField(max_length=5000,blank=True, null=True)
# 
class Domain(models.Model):
    add_domain=models.CharField(max_length=200,blank=True, null=True)
    is_live=models.BooleanField(default=False)
    def __str__(self):
        return self.add_domain
   




