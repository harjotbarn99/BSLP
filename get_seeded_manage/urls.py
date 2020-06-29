

from django.urls import path, include
from .views import home_GSM



urlpatterns = [
    path('', home_GSM, name="home-GSM"),
    path('candidates/',include('get_seeded_manage_cand.urls')),
    path('voting/',include('get_seeded_manage_voting.urls')),

]