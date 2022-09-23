from django import forms
from .models import ChapterSummary, ChapterList

class CourseList(forms.ModelForm):
    class Meta:
        model = ChapterList
        fields = ['course']

class Summary(forms.ModelForm):
    class Meta:
        model = ChapterSummary
        fields = ['chapter', 'body', 'verified']

class EditSummary(forms.ModelForm):
    class Meta:
        model = ChapterSummary
        fields = ['body', 'verified']