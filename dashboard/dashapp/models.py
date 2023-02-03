from django.db import models
from datetime import datetime


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    Phone = models.CharField(max_length=50, null=True)
    Email = models.EmailField()
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )

    name = models.CharField(max_length=50, null=True)
    Price = models.FloatField()
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    Description = models.CharField(max_length=300, null=True, blank=True)
    Date = models.DateField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),

    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name


