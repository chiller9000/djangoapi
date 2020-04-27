from django.db import models

# Create your models here.
class Spot(models.Model):
    name = models.CharField(max_length=200)
    geolocation = models.CharField(max_length=150)
    windDirection = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)

    def __str__(self):
        return self.name