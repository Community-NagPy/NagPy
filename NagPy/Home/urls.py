from django.urls import path
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

app_name = "Home"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", login, {"template_name": "nagpy/login.html"}, name="login"),
    path("logout/", logout, {"template_name": "nagpy/logout.html"}, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/<int:pk>/", views.edit_event, name="edit_event"),
    path(
        "reset_password/",
        password_reset,
        {
            "template_name": "nagpy/reset_password.html",
            "post_reset_redirect": "Home:password_reset_done",
            "email_template_name": "nagpy/reset_password_email.html",
        },
        name="reset_password",
    ),
    path(
        "reset_password/done/",
        password_reset_done,
        {"template_name": "nagpy/reset_password_done.html"},
        name="password_reset_done",
    ),
    path(
        "reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/",
        password_reset_confirm,
        {
            "post_reset_redirect": "Home:password_reset_complete",
            "template_name": "nagpy/reset_password_confirm.html",
        },
        name="password_reset_confirm",
    ),
    path(
        "reset_password/complete/",
        password_reset_complete,
        {"template_name": "nagpy/reset_password_complete.html"},
        name="password_reset_complete",
    ),
    path("events/add/", views.event_add, name="add_event"),
    path("events/", views.events_view, name="events_view"),
    path("userprofile/edit/", views.userprofile_edit, name="userprofile_edit"),
]

