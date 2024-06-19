from django.urls import path
from content.views import index, movies


urlpatterns = [
    path("", index),
    path("movies/", movies, name="movies")
]