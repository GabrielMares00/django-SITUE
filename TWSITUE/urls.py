from django.urls import path
from django.conf.urls.static import static

from base import settings
from . import views

urlpatterns = [
    path('', views.loginPage),
    path('login', views.loginPage),
    path('signup', views.signupPage),
    path('home', views.home),
    path('about', views.about),
    path('image-search', views.imageSearcher),
    path('text-search', views.textSearcher),
    path('image-uploader', views.imageUploader),
    path('upload-done-template-image', views.imageUploadedView),
    path('text-uploader', views.textUploader),
    path('logout', views.logoutView)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
