import os
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


def path_and_rename(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

# Create your models here.


class Image(models.Model):
    # id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to=path_and_rename)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 editable=False,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    keyword = models.CharField(max_length=32)
    upload_date = models.DateTimeField(auto_now=True)
