from django.shortcuts import render
from recruit.models import RecruitPost
from django.contrib.auth import get_user_model


def myclass(request):
    ids = []
    for post in RecruitPost.objects.all():
        participants = post.participants.all()
        if request.user in participants or request.user == post.user:
            ids.append(post.id)
    groups = RecruitPost.objects.filter(id__in=ids)

    return render(request,'GroupPage.html', {'groups': groups})
