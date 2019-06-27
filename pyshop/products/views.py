from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from products.templates.forms import SignUpForm


def index(request):
    return render(request, 'header.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def Contact(request):
    return render(request, 'contact.html')


def About(request):
    return render(request, 'About.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/home/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
