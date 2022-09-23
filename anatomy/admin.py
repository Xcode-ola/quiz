from django.contrib import admin
from .models import ChapterList, ChapterSummary

# Register your models here.
admin.site.register(ChapterList)
admin.site.register(ChapterSummary)