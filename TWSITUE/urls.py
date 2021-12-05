from django.urls import path

from . import views


urlpatterns = [
    path('', views.loginPage),
    path('signup', views.signupPage),
    path('home', views.home),
    path('about', views.about),
    path('image-search', views.imageSearcher),
    path('text-search', views.textSearcher),
    path('image-uploader', views.imageUploader),
    path('text-uploader', views.textUploader)
]