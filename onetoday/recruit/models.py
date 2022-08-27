from tkinter.tix import Balloon
from unicodedata import category
from django.db import models
from account.models import CustomUser

# Create your models here.
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

    def upload(self):
        self.save()

    def __str__(self):
        return self.title