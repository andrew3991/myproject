from django.contrib import admin

# Register your models here.
from .models import Task, Comments

# class TaskAdmin(admin.ModelAdmin):
# 	fields = ['article_title', ]

admin.site.register(Task)