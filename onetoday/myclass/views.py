from django.shortcuts import render
from recruit.models import RecruitPost
from django.contrib.auth import get_user_model


def myclass(request):
    User = get_user_model()
    classes = RecruitPost.objects.filter(user=User)
    return render(request,'myclass.html', {'classes':classes})