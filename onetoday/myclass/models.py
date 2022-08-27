from django.db import models
from datetime import date

class Class(models.Model):
    type = models.CharField()
    date = models.DateField(default=date.today)
    place = models.CharField()
    name = models.CharField()

    def __str__(self):
        return self.name