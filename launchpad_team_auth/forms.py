from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    registerationCode = forms.CharField(label="Registeration Code")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_registerationCode(self, *args, **kwargs):
        registerationCode = self.cleaned_data.get("registerationCode")
        if registerationCode != "test123":
            raise ValidationError("wrong code")
        return registerationCode
