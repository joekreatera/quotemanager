from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField("name", max_length=255, default="New Item", null=False)
    price = models.FloatField("price",default=0.0, null=False)
    