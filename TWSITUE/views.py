from django import forms
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from TWSITUE.forms import ImageUploadForm, AuthForm, UserCreateForm


# Create your views here.
from TWSITUE.models import Image


def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def imageSearcher(request):
    return render(request, "image-search.html", {})


def textSearcher(request):
    return render(request, "text-search.html", {})


def imageUploader(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            imageToUpload = form.save(commit=False)
            imageToUpload.uploader = request.user
            imageToUpload.save()
            imageToUpload.raw_name = imageToUpload.image.url[14:]
            imageToUpload.save()

            imageName = imageToUpload.raw_name.split('.')[0]
            imageExtension = imageToUpload.raw_name.split('.')[1]

            return redirect(imageUploadedView, imageName, imageExtension)
    else:
        form = ImageUploadForm()

    return render(request, 'image-uploader.html', {'form': form})


def imageUploadedView(request, imageUploadedName, imageUploadedExtension):
    context = {
        'image_path': imageUploadedName,
        'image_extension': imageUploadedExtension,
        'image_combined': imageUploadedName + '.' + imageUploadedExtension,
        'link_path': '127.0.0.1:8000/media/images/' + imageUploadedName + '.' + imageUploadedExtension,
        'media_path': 'media/images/' + imageUploadedName + '.' + imageUploadedExtension
    }
    return render(request, 'image-uploaded.html', context)


def textUploader(request):
    return render(request, "text-uploader.html", {})


def loginPage(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)

        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)

            return redirect(home)
    else:
        if request.user.is_authenticated:
            return redirect(home)
        else:
            form = AuthForm()

    return render(request, "login.html", {'form': form})


def signupPage(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()

            # log the user in
            login(request, user)

            return redirect(home)
    else:
        form = UserCreateForm()

    return render(request, "signup.html", {'form': form})


def logoutView(request):
    auth_logout(request)
    return redirect(loginPage)
