from django.db import models

# Create your models here.
class Movie(models.Model):
    moviename = models.CharField(max_length=100)
    directorname = models.CharField(max_length=100)
    year=models.IntegerField()


class Dirdetails(models.Model):
    name = models.CharField(max_length=100)
    movies = models.CharField(max_length=100)
    
