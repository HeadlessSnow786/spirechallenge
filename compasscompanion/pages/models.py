from django.db import models

# Create your models here.

class StartPoint(models.Model):
    startlat = models.DecimalField(decimal_places=6, max_digits=9) # all are taken from the user input on the website page
    startlong = models.DecimalField(decimal_places=6, max_digits=9)
    time = models.CharField(max_length=25) 

    endlat = models.DecimalField(decimal_places=6, max_digits=9)
    endlong = models.DecimalField(decimal_places=6, max_digits=9)
    #end_time = models.CharField(max_length=25)
    #other parameters ? probably only need the time here
