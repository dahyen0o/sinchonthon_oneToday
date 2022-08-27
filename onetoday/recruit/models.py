from django.db import models
from account.models import CustomUser
from myclass.models import *
from datetime import datetime

# Create your models here.

class Vote(models.Model):
    recommend_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    vote_user = models.ManyToManyField(CustomUser, blank=True)


class RecruitPost(models.Model):
    place_list = {
        ('종로구', '종로구'), ('중랑구', '중랑구'), ('서대문구', '서대문구'),
        ('중구', '중구'), ('성북구', '성북구'), ('마포구', '마포구'),
        ('용산구', '용산구'), ('강북구', '강북구'), ('양천구', '양천구'),
        ('성동구', '성동구'), ('도봉구', '도봉구'), ('강서구', '강서구'),
        ('광진구', '광진구'), ('노원구', '노원구'), ('구로구', '구로구'),
        ('동대문구', '동대문구'), ('은평구', '은평구'), ('금천구', '금천구'),
        ('영등포구', '영등포구'), ('동작구', '동작구'), ('관악구', '관악구'),
        ('서초구', '서초구'), ('강남구', '강남구'), ('송파구', '송파구'),
        ('강동구', '강동구'),
    }
    category_list = {
        ('요리', '요리'), ('뷰티', '뷰티'), ('키즈', '키즈'),
        ('수공예', '수공예'), ('모임', '모임'), ('DIY', 'DIY'),
        ('플라워', '플라워'), ('정규', '정규'),
        ('미술', '미술'), ('음악', '음악'),
        ('액티비티', '액티비티'), ('라이프스타일', '라이프스타일'),
    }

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    start_date = models.DateField(auto_now_add=True)
    finish_date = models.DateField()
    place = models.CharField(max_length=15, choices=place_list)
    category = models.CharField(max_length=15, choices=category_list, null=True)
    total_people = models.IntegerField()
    curr_people = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(CustomUser, related_name='participate', blank=True)
    vote = models.ManyToManyField(Vote, blank=True)

    def __str__(self):
        return self.name