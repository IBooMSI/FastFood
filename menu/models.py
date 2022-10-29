from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.FileField(upload_to='pictures/')
    price = models.FloatField()

    def __str__(self) -> str:
        return str(self.name)




