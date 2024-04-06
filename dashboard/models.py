from django.db import models

# Create your models here.


class Patient(models.Model):
    bedno = models.IntegerField()
    patientid = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=200)
    doctorname = models.CharField(max_length=200)
    aadharno = models.PositiveBigIntegerField()
    deviceid = models.IntegerField(unique=True)
    slug = models.SlugField(unique=True)
