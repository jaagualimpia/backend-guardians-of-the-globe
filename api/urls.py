from django.urls import path

from api import views

urlpatterns = [
    path("", views.index, name="index"),
    path("heroes", views.heroes, name="heroes"),
    path("heroes/<int:id>", views.hero, name="hero"),
    path("matches", views.matches, name="matches"),
    path("matches/<int:id>", views.match, name="match"),
    path("sponsors", views.sponsors, name="sponsors"),
    path("sponsors/<int:id>", views.sponsor, name="sponsor"),
    path("villains", views.villains, name="villains"),
    path("villains/<int:id>", views.villain, name="villain"),
]
