from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200) 
    author = models.CharField(max_length=100) 
    description=models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)  # Set a default Book ID here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


