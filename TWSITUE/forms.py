from django import forms
from TWSITUE.models import Image


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image', 'keyword']
