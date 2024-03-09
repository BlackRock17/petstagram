from django.urls import path, include

from petstagram.accounts.views import (RegisterUserView, SignInUserView,
                                       ProfileDetailsView, ProfileUpdateView,
                                       ProfileDeleteView, signout_user)

urlpatterns = (
    path("register/", RegisterUserView.as_view(), name="register_user"),
    path("login/", SignInUserView.as_view(), name="signin_user"),
    path("signout/", signout_user, name="signout_user"),

    path("profile/<int:pk>/", include([
        path("", ProfileDetailsView.as_view(), name="details_profile"),
        path("edit/", ProfileUpdateView.as_view(), name="edit_profile"),
        path("delete/", ProfileDeleteView.as_view(), name="delete_profile"),
    ]))
)
