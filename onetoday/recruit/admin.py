from django.contrib import admin
from .models import *

admin.site.register(RecruitPost)

@admin.register(Vote)
class DayAdmin(admin.ModelAdmin):
	list_display = ['id']
	list_display_links = ['id']

