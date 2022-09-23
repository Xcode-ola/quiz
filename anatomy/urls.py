from django.urls import path
from .views import ana_index, lowerlimb, AddCourse, AddSummary, UpdateSummary

urlpatterns = [
    path('', ana_index, name="ana_index"),
    path('lowerlimb/', lowerlimb, name="lowerlimb"),
    path('addcourse/', AddCourse.as_view(), name="add_course"),
    path('addsummary/', AddSummary.as_view(), name="add_summary"),
    path('edit/<int:pk>/', UpdateSummary.as_view(), name="edit_summary")
]