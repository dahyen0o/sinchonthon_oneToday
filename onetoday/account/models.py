from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="blog_photo")