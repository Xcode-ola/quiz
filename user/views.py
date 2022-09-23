from django.shortcuts import redirect, render
from django.contrib.auth.models import auth, User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import ProfileEdit

# Create your views here.
def register(response):
    if response.method == "POST":
        username = response.POST['username']
        email = response.POST['email']
        password1 = response.POST['password1']
        password2 = response.POST['password2']

        if password1 == password2:

            if User.objects.filter(email=email).exists():
                messages.info(response, "This email already exists")
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(response, "This username already exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password1=password1, password2=password2)
                user.save()
                auth.login(response, user)
                return redirect('index')

        else:
            messages.info(response, "The passwords do not match")
            return redirect('register')

    return render(response, 'registration/register.html')

def login(response):
    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(response, user)
            return redirect('index')

        else:
            messages.info(response, "Invalid credentials")
            return redirect('login')

    return render(response, 'registration/login.html')

def logout(response):
    auth.logout(response)
    return redirect('index')

@login_required(login_url="/user/login/")
def profile_page(response):
    return render(response, 'user/profile.html')

class profile_edit(UpdateView):
    model = User
    template_name = 'user/edit_profile.html'
    form_class = ProfileEdit
    success_url = reverse_lazy('profile')