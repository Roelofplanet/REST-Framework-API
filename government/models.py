from django.db import models

class GovernmentData(models.Model):
    naam = models.CharField(max_length=100)
    inwoners = models.CharField(max_length=20)
    oppervlakte = models.CharField(max_length=20)
    hoofdplaats = models.CharField(max_length=100)

    def __str__(self):
        return self.naam
