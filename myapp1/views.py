from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, User_fb, User_linkedin
from passlib.hash import pbkdf2_sha256


# Create your views here.
def home(request):
    return render(request, 'index.html')


def landing(request):
    return render(request, 'landing.html')


def login(request):
    return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')


class UserCreateView(CreateView):
    model = User
    template_name = 'login.html'
    fields = ('email', 'password')


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})


class UserCreateView_fb(CreateView):
    model = User_fb
    template_name = 'fb_signup.html'
    fields = ('email', 'password')


class UserCreateView_linked_in(CreateView):
    model = User_linkedin
    template_name = 'linkedin_signup.html'
    fields = ('email', 'password')
