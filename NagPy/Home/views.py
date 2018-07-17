from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from Home.forms import (
    RegisterForm,
    EditProfileForm,
    AddEventForm,
    EditUserProfileForm,
    EditEventForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from .models import Event, Userprofile

# Create your views here.


def home(request):
    return render(request, "nagpy/home.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("Home:home"))
        else:
            return render(request, "nagpy/register.html", {"form": form})

    else:
        form = RegisterForm()
        args = {"form": form}
        return render(request, "nagpy/register.html", args)


def view_profile(request):
    args = {"user": request.user}
    return render(request, "nagpy/profile_view.html", args)


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse("Home:view_profile"))
    else:
        form = EditProfileForm(instance=request.user)
        args = {"form": form}
        return render(request, "nagpy/edit_profile.html", args)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse("Home:view_profile"))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {"form": form}
        return render(request, "nagpy/change_password.html", args)


def event_add(request):
    if request.method == "POST":
        form = AddEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.manager = request.user
            event.save()
            return redirect(reverse("Home:events_view"))
        else:
            return render(request, "nagpy/event_add.html", {"form": form})
    else:
        form = AddEventForm()
        return render(request, "nagpy/event_add.html", {"form": form})


def events_view(request):
    event_list = Event.objects.all()
    args = {"events": event_list}
    return render(request, "nagpy/events_view.html", args)


def userprofile_edit(request):
    ins = get_object_or_404(Userprofile, pk=request.user.userprofile.pk)

    if request.method == "POST":
        form = EditUserProfileForm(request.POST, request.FILES, instance=ins)
        if form.is_valid():
            instance = form.save(commit=False)
            # userprofile.user = request.user
            instance.save()
            return redirect(reverse("Home:view_profile"))
        else:
            context = {
                "description": ins.description,
                "city": ins.city,
                "website": ins.website,
                "instance": ins,
                "form": form,
            }
            return render(request, "nagpy/userprofile_edit.html", context)
    else:
        form = EditUserProfileForm(instance=ins)
        context = {
            "description": ins.description,
            "city": ins.city,
            "website": ins.website,
            "instance": ins,
            "form": form,
        }
        return render(request, "nagpy/userprofile_edit.html", context)


def dashboard(request):
    event_list = Event.objects.filter(manager_id=request.user).all()
    args = {"events": event_list}
    return render(request, "nagpy/dashboard.html", args)


def edit_event(request, pk):
    usr = get_object_or_404(Event, pk=pk)

    if usr.manager == request.user:
        if request.POST:
            form = EditEventForm(request.POST, instance=usr)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect(reverse("Home:dashboard"))
            else:
                args = {"usr": usr, "pk": pk, "form": form}
                return render(request, "nagpy/edit_event.html", args)
        else:
            form = EditEventForm(instance=usr)
            args = {"usr": usr, "pk": pk, "form": form}
            return render(request, "nagpy/edit_event.html", args)
    else:
        return redirect(reverse("Home:dashboard"))

