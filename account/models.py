import email
from operator import truediv
from telnetlib import STATUS
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 


class product(models.Model):
    CATEGORY = (
        ('dakheli', 'dakheli'),
        ('khareji', 'khareji'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(tag)

    def __str__(self):
        return self.name


class order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('out for delivery', 'out for delivery'),
        ('delivered', 'delivered'),
    )

    customer = models.ForeignKey(customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)
