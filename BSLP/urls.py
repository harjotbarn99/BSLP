
from django.urls import path, include
from.views import homepage_BSLP

urlpatterns = [
     path('', homepage_BSLP, name="home-BSLP"),
     path('get-seeded/', include('get_seeded.urls')),

]
