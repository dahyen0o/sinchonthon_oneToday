from tkinter import CASCADE
from django.db import models
from account.models import CustomUser
from myclass.models import *

# Create your models here.

class Vote(models.Model):
    recommend_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    vote_user = models.ManyToManyField(CustomUser, blank=True)


class RecruitPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    place = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    total_people = models.IntegerField()
    curr_people = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vote = models.ManyToManyField(Vote, blank=True)

    def __str__(self):
        return self.title
