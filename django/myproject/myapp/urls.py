from django.urls import path

from myapp.views import indes
urlpatterns = [
    path("",indes)
]
