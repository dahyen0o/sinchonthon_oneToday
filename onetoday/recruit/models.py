from django.db import models
from account.models import CustomUser
from myclass.models import *

# Create your models here.

class Vote(models.Model):
    recommend_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    vote_user = models.ManyToManyField(CustomUser, blank=True)


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
    name = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    place = models.CharField(max_length=15, choices=place_list)
    category = models.CharField(max_length=15, choices=category_list)
    total_people = models.IntegerField()
    curr_people = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(CustomUser, related_name='participate')
    vote = models.ManyToManyField(Vote, blank=True)

    def __str__(self):
        return self.name