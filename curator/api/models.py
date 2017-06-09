from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Product(models.Model):
    id
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.TextField(null=True)

class Campaign(models.Model):
    id
    name = models.CharField(max_length=255)
    description = models.TextField()
    occation = models.CharField(max_length=255)
    offer_valid_till = models.DateTimeField()
