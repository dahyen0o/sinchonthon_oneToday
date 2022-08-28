"""onetoday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account import views as account_views
from discuss import views as discuss_views
from myclass import views as myclass_views
from recruit import views as recruit_views

from discuss.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recruit_views.mainlist, name='mainlist'),
    path('more/', recruit_views.search, name='search'),

    path('recruit_post/', recruit_views.post, name='post'),
    path('recruit_detail/<int:post_id>/', recruit_views.detail, name='detail'),

    path('discuss/<int:pk>/', discuss_views.recommend, name='recommend'),
    path('board/<int:pk>/', discuss_views.board, name='board'),
    path('posting/<int:pk>/', discuss_views.posting, name='posting'),

    path('poll/<int:gr_pk>/<int:cl_pk>/', discuss_views.poll, name='poll'),

    path('myclass/', myclass_views.myclass, name='myclass'),

    path('postform/',recruit_views.postform, name='postform'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
