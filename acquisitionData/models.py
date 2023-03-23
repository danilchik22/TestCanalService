from django.db import models

# Create your models here.
class Order(models.Model):
    number_order = models.IntegerField(unique=True)
    price = models.FloatField()
    price_in_ruble = models.FloatField()
    date_of_suply = models.DateTimeField()
    
