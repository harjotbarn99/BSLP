from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home_GSM(request):
    map ={
        'title': "Home - Get seeded Manage"
    }
    return render(request, "get_seeded_manage/home_GSM.html",map)
