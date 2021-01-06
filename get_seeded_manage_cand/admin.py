from django.contrib import admin
from .models import Candidate, CandidatePhoto

# Register your models here.

admin.site.register(Candidate)
admin.site.register(CandidatePhoto)