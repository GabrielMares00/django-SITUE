from django.urls import path

from . import views


urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('image-search', views.imageSearcher),
    path('text-search', views.textSearcher)
]