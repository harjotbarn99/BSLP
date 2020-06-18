

from django.urls import path, include
from .views import votingPage_GSV



urlpatterns = [
    path('', votingPage_GSV, name="home-GSV"),



]