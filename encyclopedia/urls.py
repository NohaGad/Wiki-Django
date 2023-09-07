from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/create", views.create, name="create"),
    path("wiki/random", views.randomPage, name="random"),
    path("wiki/edit/<str:title>", views.editEntry, name="edit"),
    path("wiki/<str:title>", views.details, name="details"),
]
