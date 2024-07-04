from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("upload", views.upload, name="upload"),
  path("files", views.files, name="files"),
  path("about", views.about, name="about"),
  path("graphs", views.graphs, name="graphs"),
  path("data", views.data, name="data"),
  path("logs", views.logs, name="logs"),
  path("user", views.user, name="user"),
]