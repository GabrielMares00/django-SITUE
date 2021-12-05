from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def imageSearcher(request):
    return render(request, "image-search.html", {})


def textSearcher(request):
    return render(request, "text-search.html", {})


def imageUploader(request):
    return render(request, "image-uploader.html", {})


def textUploader(request):
    return render(request, "text-uploader.html", {})


def loginPage(request):
    return render(request, "login.html", {})


def signupPage(request):
    return render(request, "signup.html", {})
