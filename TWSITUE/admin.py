from django.contrib import admin

from TWSITUE.models import Image


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'keyword', 'uploader', 'upload_date')


admin.site.register(Image, ImageAdmin)
