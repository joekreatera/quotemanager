from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField("name", max_length=200, null=False, default="Client Name")
    rfc =  models.CharField("rfc", max_length=13, null=False, default="XAXX010101ABC")

    def __str__(self):
        return f"{self.name} ({self.rfc})"