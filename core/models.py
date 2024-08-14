from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    stock = models.ForeignKey(Stock, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)
