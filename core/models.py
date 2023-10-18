from django.db import models

# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=100, null=True)
    price = models.IntegerField()
    rating = models.FloatField(max_length=50)

    def __str__(self):
        return self.name
