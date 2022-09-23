from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .models import ChapterList, ChapterSummary
from .forms import CourseList, Summary, EditSummary

# Create your views here.
@login_required(login_url="/user/login/")
def ana_index(response):
    context = {
        'chapters':ChapterList.objects.all(),
    }
    return render(response, 'anatomy/index.html', context)

def lowerlimb(response):
    return render(response, 'lowerlimb/index.html')

class AddCourse(CreateView):
    model = ChapterList
    template_name = 'anatomy/add_course.html'
    form_class = CourseList
    success_url = reverse_lazy('ana_index')

class AddSummary(CreateView):
    model = ChapterSummary
    template_name = 'anatomy/add_summary.html'
    form_class = Summary
    success_url = reverse_lazy('ana_index')

class UpdateSummary(UpdateView):
    model = ChapterSummary
    template_name = 'anatomy/add_summary.html'
    form_class = EditSummary
    success_url = reverse_lazy('ana_index')