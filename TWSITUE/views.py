from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].label = ""


class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

        for fieldname in ['username', 'password']:
            self.fields[fieldname].label = ""

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
