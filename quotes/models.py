from django.db import models
from clients.models import Client
from items.models import Item
from datetime import datetime
# Create your models here.

class Quote(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    date = models.DateField("creation_date", default = datetime.today )
    items = models.ManyToManyField(Item)