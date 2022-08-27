from django.db import models
from datetime import date

class Class(models.Model):
    type = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    place = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name