from django import forms
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from TWSITUE.forms import ImageUploadForm


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label='Email',
                             error_messages={'exists': 'Sorry, but this email is already used.'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

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

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


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
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect(imageUploadedView)
    else:
        form = ImageUploadForm()

    return render(request, 'image-uploader.html', {'form': form})


def imageUploadedView(request):
    return HttpResponse('successfully uploaded')


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
