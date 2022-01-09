from django.contrib import admin

from TWSITUE.models import Image, Text


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'raw_name', 'keyword', 'uploader', 'upload_date')

    def save_model(self, request, obj, form, change):
        obj.uploader = request.user
        super().save_model(request, obj, form, change)


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'generated_name', 'keyword', 'uploader', 'upload_date')

    def save_model(self, request, obj, form, change):
        obj.uploader = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Image, ImageAdmin)
admin.site.register(Text, TextAdmin)
