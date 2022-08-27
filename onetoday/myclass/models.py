from django.db import models
from datetime import date

class Class(models.Model):
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

    type = models.CharField(max_length=200, choices=category_list)
    date = models.DateField(default=date.today)
    place = models.CharField(max_length=200, choices=place_list)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name