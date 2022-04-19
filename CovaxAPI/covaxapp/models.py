from django.db import models

# Create your models here.
class Facilities(models.Model):
    County = models.CharField(max_length=250, null=True)
    Sub_County = models.CharField(max_length=250, null=True)
    Health_Facility_Name = models.CharField(max_length=250, null=True)
    Latitudes = models.DecimalField(max_length=100, max_digits=100, decimal_places=12, null=True)
    Longitudes = models.DecimalField(max_length=100, max_digits=100, decimal_places=12, null=True)