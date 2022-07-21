from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Customer(models.Model):

    first_name = models.CharField(max_length=150)

    def __str__(self):

        return self.first_name


class Order(models.Model):

    price_total = models.FloatField()
    customer_FK = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(default=timezone.now, null=False)
    brand_id = models.IntegerField()
    reference = models.CharField(max_length=150)


class Product(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):

        return self.name


class Delivery(models.Model):

    order_FK = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipped = models.BooleanField()
    delivery_product = models.ManyToManyField(Product, through='DeliveryProduct')


class DeliveryProduct(models.Model):

    product_FK = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_delivery_product')
    delivery_FK = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='delivery_delivery_product')
    quantity = models.IntegerField()


