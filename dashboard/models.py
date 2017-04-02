from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Diner(models.Model):
    address = models.CharField(max_length=255)
    tlf = models.CharField(max_length=255)
    image = models.ImageField(upload_to='MEDIA_ROOT')

class UserWorksAtDiner(models.Model):
    user = models.ForeignKey(User)
    diner = models.ForeignKey(Diner)


class Table(models.Model):
    pos = models.CharField(max_length=255) #x y
    occupied = models.BooleanField(default=False)
    diner = models.ForeignKey(Diner)


class Customer(models.Model):
    order = models.CharField(max_length=512)
    table = models.ForeignKey(Table)

class Item(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=10)
