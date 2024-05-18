
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def _str_(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)

    def _str_(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name