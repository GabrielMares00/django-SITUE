import os
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars


def path_and_rename_for_image(instance, filename):
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
    image = models.ImageField(upload_to=path_and_rename_for_image,
                              null=False)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 editable=False,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    keyword = models.CharField(max_length=32,
                               null=True,
                               blank=True)
    raw_name = models.CharField(max_length=32,
                                null=True)
    upload_date = models.DateTimeField(auto_now=True)


class Text(models.Model):
    title = models.CharField(max_length=128,
                             blank=False)
    text = models.TextField(blank=False)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 editable=False,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    keyword = models.CharField(max_length=32,
                               null=True,
                               blank=True)
    generated_name = models.CharField(max_length=32,
                                      default=uuid4().hex)
    upload_date = models.DateTimeField(auto_now=True)

    @property
    def short_description(self):
        return truncatechars(self.text, 100)
