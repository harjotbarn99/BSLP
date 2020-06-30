from django.urls import path, include
from .views import home_getSeeded


urlpatterns = [
    path("", home_getSeeded, name="home-getSeeded"),
    path("manage/", include("get_seeded_manage.urls")),
    path("vote/", include("get_seeded_voting.urls")),
]

