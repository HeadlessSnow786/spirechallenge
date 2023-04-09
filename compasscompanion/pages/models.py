from django.db import models

# Create your models here.

class StartPoint(models.Model):
    latitude = models.DecimalField(decimal_places=6, max_digits=9) # all are taken from the user input on the website page
    longitude = models.DecimalField(decimal_places=6, max_digits=9)
    time = models.CharField(max_length=25) 
    #other parameters ? probably only need the time here

class EndPoint(models.Model):
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)
    end_time = models.CharField(max_length=25) # should be estimated by Arya's code
    #other parameters