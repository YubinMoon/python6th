from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.BooksModelView.as_view(), name="index"),
]
