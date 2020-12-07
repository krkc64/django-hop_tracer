from django.db import models

# Create your models here.
class Details(models.Model):

    FullName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    Postcode = models.CharField(max_length=100)
    TTN = models.CharField(max_length=100)
    Result = models.CharField(max_length=100)

class HomeTestKit(models.Model):
    TTN_code = models.CharField(max_length=10)
    used = models.BooleanField(default=False)

class Admin_credentials(models.Model):
    username = models.CharField(max_length=100)
    password_hash = models.TextField()

#from django.db.models import Count

 #Details.objects.values('Result').annotate(c=Count('Result'))

 #Details.objects.filter(Age__range=["20", "30"])

#Details.objects.filter(Age__range=["20", "30"]).values('Result').annotate(c=Count('Result'))

