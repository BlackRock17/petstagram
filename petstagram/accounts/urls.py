from django.urls import path, include

from petstagram.accounts.views import RegisterUserView, SignInUserView, details_profile, edit_profile, delete_profile, \
    signout_user

urlpatterns = (
    path("register/", RegisterUserView.as_view(), name="register_user"),
    path("login/", SignInUserView.as_view(), name="signin_user"),
    path("signout/", signout_user, name="signout_user"),

    path("profile/<int:pk>/", include([
        path("", details_profile, name="details_profile"),
        path("edit/", edit_profile, name="edit_profile"),
        path("delete/", delete_profile, name="delete_profile"),
    ]))
)
