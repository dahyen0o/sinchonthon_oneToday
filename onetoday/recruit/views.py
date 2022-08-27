from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import *

# Create your views here.
def mainlist(request):
    posts = RecruitPost.objects.filter().order_by('-created_at')
    return render(request, 'mainlist.html', {'posts':posts})

def post(request):
    recruit_post = RecruitPost()
    if request.method == 'POST':
        recruit_post.user = get_user_model()
        recruit_post.title = request.POST['title']
        recruit_post.content = request.POST['content']
        recruit_post.start_date = request.POST['start_date']
        recruit_post.finish_date = request.POST['finish_date']
        recruit_post.place = request.POST['place']
        recruit_post.category = request.POST['category']
        recruit_post.total_people = request.POST['total_people']
        recruit_post.curr_people = request.POST['curr_people']
        recruit_post.save()

        return redirect('mainlist')
    
def detail(request):
    # 해당 게시글에 지원
    if request.method == 'POST':
        user = get_user_model()
        recruit_post = RecruitPost.objects.get(title=request.POST['title'])
        recruit_post.curr_people += 1
        recruit_post.save()
        return redirect('detail')
    # 해당 게시글 출력
    elif request.method == 'GET':
        return render(request, 'detail.html', {'detail': RecruitPost.objects.get(title=request.POST['title'])})
