from tokenize import group
from django.shortcuts import render
from recruit.models import RecruitPost
from django.contrib.auth import get_user_model


def myclass(request):
    User = get_user_model()
    groups = RecruitPost.objects.filter(user=request.user)
    for post in RecruitPost.objects.all():
        participants = post.participants.all()
        if request.user in participants and post not in groups:
            groups.add(post)
    return render(request,'myclass.html', {'groups': groups})