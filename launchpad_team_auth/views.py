from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.


def register_LTA(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Your account has been created! with the username {username}, you are now able to log in",
            )
            return redirect("login-LTA")
    else:
        form = UserRegisterForm()
    return render(
        request,
        "launchpad_team_auth/register_LTA.html",
        {"form": form, "title": "Register - Get Seeded Team"},
    )

