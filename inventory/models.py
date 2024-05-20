
from django.db import models






class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='image_book',blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
 
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=60)
    bio = models.TextField(blank=True , null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name