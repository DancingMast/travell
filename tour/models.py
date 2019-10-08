from django.db import models

# Create your models here.


class plotsector(models.Model):
    sec_name = models.CharField(max_length=100)
    contrib = models.FloatField()


class userfavs(models.Model):
    username = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    town = models.CharField(max_length=50)

class comfavs(models.Model):
    town = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    count = models.IntegerField(default= 0)