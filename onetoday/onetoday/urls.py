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

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', recruit_views.mainlist, name='mainlist'),
    path('recruit_post/', recruit_views.post, name='post'),
    path('recruit_detail/<int:post_id>', recruit_views.detail, name='detail'),

    path('discuss/<int:pk>', recommend, name='recommend'),
    path('poll/<int:gr_pk>/<int:cl_pk>', poll, name='poll'),
]
