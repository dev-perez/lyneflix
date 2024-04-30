from django.urls import path
from content.views import index


urlpatterns = [
    path("", index)
]