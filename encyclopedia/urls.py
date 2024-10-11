from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/",views.search,name="search"),
    path("new/", views.new, name="new"),
    path("edit/", views.edit, name="edit"),
    path("save/", views.save, name="save"),
    path("rand/", views.rand, name="rand"),
]
