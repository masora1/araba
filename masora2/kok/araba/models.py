from django.db import models

class Car(models.Model):
    Model = models.CharField(max_length=50)
    Ulke = models.CharField(max_length=50)
    Fiyat = models.IntegerField()
    Km = models.IntegerField(null=True)
    Tarih = models.DateField()