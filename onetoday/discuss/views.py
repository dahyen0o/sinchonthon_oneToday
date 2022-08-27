from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from recruit.models import RecruitPost
from myclass.models import Class
from account.models import CustomUser

# Create your views here.

def recommend(request, pk):
    group = get_object_or_404(RecruitPost, pk=pk)
    start_date = group.start_date
    finish_date = group.finish_date
    classes = Class.objects.filter(type=group.category, place=group.place).filter(date__range=[start_date, finish_date])
    participants = group.participants.all()
    return render(request, 'hy.html', {'filtered_classes' : classes, 'group': group, 'participants' : participants})


def poll(request, gr_pk, cl_pk):
    group = get_object_or_404(RecruitPost, pk=gr_pk)
    votes = group.vote.get(pk=cl_pk)
    user = get_object_or_404(CustomUser, pk=1)
    if user not in votes.vote_user.all():
        votes.vote_user.add(user)
    else:
        votes.vote_user.remove(user)
    return redirect('recommend', gr_pk)
