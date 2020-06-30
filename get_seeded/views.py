from django.shortcuts import render

# Create your views here.


def home_getSeeded(request):
    map = {"title": "Home - Get seeded "}
    return render(request, "get_seeded/home_getSeeded.html", map)

