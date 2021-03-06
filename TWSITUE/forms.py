from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from TWSITUE.models import Image, Text


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


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'keyword']

    def __init__(self, *args, **kwargs):
        super(ImageUploadForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['image'].widget.attrs['hidden'] = True
        self.fields['image'].label = "Select Your Image"
        self.fields['keyword'].widget.attrs['placeholder'] = "Keyword (optional)"
        self.fields['keyword'].label = ""


class TextUploadForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['title', 'text', 'keyword']

    def __init__(self, *args, **kwargs):
        super(TextUploadForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['title'].label = ""
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['text'].label = ""
        self.fields['text'].widget.attrs['class'] = 'textArea'
        self.fields['text'].widget.attrs['placeholder'] = 'Text'
        self.fields['keyword'].widget.attrs['placeholder'] = "Keyword (optional)"
        self.fields['keyword'].label = ""
