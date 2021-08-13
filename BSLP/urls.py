from django.urls import path, include
from .views import homepage_BSLP

urlpatterns = [
    path("home", homepage_BSLP, name="home-BSLP"),
    path("",  include("get_seeded_voting.urls")),
    path("get-seeded/", include("get_seeded.urls")),
]
