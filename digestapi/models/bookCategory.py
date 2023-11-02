from django.db import models

class BookCategory(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="categories")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="books")
    date = models.DateField(auto_now_add=True)