from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ChapterList(models.Model):
    course = models.CharField(max_length=255)

    def __str__(self):
        return self.course

class ChapterSummary(models.Model):
    chapter = models.ForeignKey(ChapterList, related_name="summary", on_delete=models.CASCADE)
    body = RichTextField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.chapter

class AnatomyQuiz(models.Model):
    pass