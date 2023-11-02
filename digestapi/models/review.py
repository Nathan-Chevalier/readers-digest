from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_rating_range(rating):
    if not 1 <= rating <= 10:
        raise ValidationError("Value must be between 1 and 10.") #? Conditional to set the review range from 1-5

class Review(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(max_length=2, validators=[validate_rating_range]) #? Specifies positive integer
    comment = models.CharField(max_length=2000)
    date = models.DateField(auto_now_add=True) #? auto_add_now sets the date upon creation and does not update
