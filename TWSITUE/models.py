from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Image(models.Model):
    # id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    uploader = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=32)
