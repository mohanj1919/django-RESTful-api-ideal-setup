from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Product(models.Model):
    id
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.TextField(null=True)
