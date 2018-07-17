from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Event, Userprofile
from django.conf import settings


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    help_texts = {
        "password": "1> Your password can't be too similar to your other personal information 2> your password must contain at least 8 characters 3> your password can't be commonaly used password 4> your password can't be entirely numeric"
    }

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
        exclude = ['username', 'password']
    def clean_password(self):
        return ""

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        help_texts = {
            "venue": "add detailed venue address",
            "time": "Time format is hr:min",
            "date": "mm/dd/yyyy",
        }
        fields = ("name", "city", "description", "venue", "date", "time", "contact")


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        exclude = ["user", "phone"]


class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("name", "city", "time", "date", "description", "venue", "contact")
