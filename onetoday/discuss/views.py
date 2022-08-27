from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from recruit.models import RecruitPost
from myclass.models import Class

# Create your views here.

def recommend(request, pk):
    group = get_object_or_404(RecruitPost, pk=pk)
    start_date = group.start_date
    finish_date = group.finish_date
    classes = Class.objects.filter(type=group.category, place=group.place).filter(date__range=[start_date, finish_date])

    return render(request, 'hy.html', {'classes' : classes})

