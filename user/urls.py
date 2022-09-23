from django.urls import path
from .views import register, login, logout, profile_page, profile_edit

urlpatterns = [
    path('signup/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('profile/', profile_page, name="profile"),
    path('<int:pk>/edit/', profile_edit.as_view(), name="profile_edit"),
]