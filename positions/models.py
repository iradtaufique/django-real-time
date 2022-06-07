from pyexpat import model
from statistics import mode
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)



class Position(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    price = models.CharField(max_length=200)
    rank = models.CharField(max_length=20)
    market_cap = models.CharField(max_length=200)


    def __str__(self):
        return str(self.name)
