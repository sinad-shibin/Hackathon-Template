from django.db import models
from django.utils import timezone

# Create your models here.
class Books(models.Model) :
    bookname = models.CharField(max_length=20)
    bookID = models.CharField(max_length=20,unique=True)
    author = models.CharField(max_length=20)
    price = models.FloatField()
    genre = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50)


