from django.db import models
from account.models import CustomUser

# Create your models here.
class RecruitPost(models.Model):
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

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    place = models.CharField(max_length=15, choices=place_list)
    category = models.CharField(max_length=15, choices=category_list)
    total_people = models.IntegerField()
    curr_people = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title