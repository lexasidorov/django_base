from django.db import models
from django.contrib.auth.models import User


# Using default django User.
# No need in User model here.

class Stock(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.address}'


class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.name}'


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    stock = models.ForeignKey(Stock, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)


    def __str__(self):
        return f'{self.name}, {self.category}'
