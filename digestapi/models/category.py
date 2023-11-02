from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(
        "Book",
        through='BookCategory',
        related_name="categories"
    )