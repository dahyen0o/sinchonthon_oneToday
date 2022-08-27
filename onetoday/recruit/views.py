from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import *

# Create your views here.
def mainlist(request):
    posts = RecruitPost.objects.filter().order_by('-created_at')
    return render(request, 'MainPage.html', {'posts':posts})

def post(request):
    recruit_post = RecruitPost()
    if request.method == 'POST':
        recruit_post.user = get_user_model()
        recruit_post.name = request.POST['name']
        recruit_post.content = request.POST['content']
        recruit_post.start_date = request.POST['start_date']
        recruit_post.finish_date = request.POST['finish_date']
        recruit_post.place = request.POST['place']
        recruit_post.category = request.POST['category']
        recruit_post.total_people = request.POST['total_people']
        recruit_post.participants.add(get_user_model())

        start_date = recruit_post.start_date
        finish_date = recruit_post.finish_date
        recommend_class = Class.objects.filter(type=recruit_post.category, place=recruit_post.place).filter(date__range=[start_date, finish_date])

        for rc in recommend_class:
            vote = Vote.objects.create(recommend_class=rc)
            recruit_post.vote.add(vote)

        recruit_post.save()

        return redirect('mainlist')
    
def detail(request, post_id):
    # 해당 게시글에 지원
    if request.method == 'POST':
        recruit_post = get_object_or_404(RecruitPost, pk=post_id)
        recruit_post.curr_people += 1
        recruit_post.participants.add(request.user)
        recruit_post.save()
        return redirect('detail', post_id)
    # 해당 게시글 출력
    else:
        return render(request, 'detail.html', {'detail': get_object_or_404(RecruitPost, pk=post_id)})
