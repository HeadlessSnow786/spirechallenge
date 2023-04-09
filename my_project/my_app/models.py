from django.db import models

# Create your models here.
class Coordinates(models.Model):
    start_latitude = models.DecimalField(decimal_places=6, max_digits=9)
    start_longitude = models.DecimalField(decimal_places=6, max_digits=9)

    end_latitude = models.DecimalField(decimal_places=6, max_digits=9)
    end_longitude = models.DecimalField(decimal_places=6, max_digits=9)
 
    time = models.CharField(max_length=25, default='2023-04-8T12:00:00')