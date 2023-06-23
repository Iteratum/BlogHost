from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("BlogHost", views.BlogHost, name="BlogHost")
]
