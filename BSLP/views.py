from django.shortcuts import render

# Create your views here.


def homepage_BSLP(request):
    map = {
        "title": "HomePage - BlackStone LaunchPad At UB"
    }
    return render(request,"BSLP/home_BSLP.html",map)