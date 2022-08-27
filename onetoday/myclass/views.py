from tokenize import group
from django.shortcuts import render
from recruit.models import RecruitPost
from django.contrib.auth import get_user_model


def myclass(request):
    User = get_user_model()
    groups = RecruitPost.objects.filter(user=request.user)
    return render(request,'myclass.html', {'groups': groups})