from django.urls import path
from . import views

urlpatterns = [
    path("", views.helloWorld, name="hello"),
    path("about", views.about, name="about")
]