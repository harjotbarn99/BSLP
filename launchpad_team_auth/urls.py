from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
)
from .views import register_LTA


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="launchpad_team_auth/login_LTA.html"),
        name="login-LTA",
    ),
    path("register/", register_LTA, name="register-LTA"),
    path(
        "logout/",
        LogoutView.as_view(template_name="launchpad_team_auth/logout_LTA.html"),
        name="logout-LTA",
    ),
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="launchpad_team_auth/passwordReset_LTA.html"
        ),
        name="passwordReset-LTA",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="launchpad_team_auth/passwordResetDone_LTA.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="launchpad_team_auth/passwordResetConfirm_LTA.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(
            template_name="launchpad_team_auth/passwordResetComplete_LTA.html"
        ),
        name="password_reset_complete",
    ),
]

