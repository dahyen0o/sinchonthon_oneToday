from django.db import models
from datetime import date

class Class(models.Model):
    place_list = {
        ('mapo-gu', '마포구'),
        ('seodaemoon-gu', '서대문구'),
        ('anyang-si', '안양시')
    }
    category_list = {
        ('perfume', '향수'),
        ('leather', '가죽'),
        ('climbing', '클라이밍'),
        ('ceramic', '도자기'),
        ('soap', '비누')
    }

    type = models.CharField(max_length=200, choices=category_list)
    date = models.DateField(default=date.today)
    place = models.CharField(max_length=200, choices=place_list)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name