from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from petstagram.accounts.forms import PetstagramUserCreationForm
from petstagram.accounts.models import Profile


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/login-page.html"
    redirect_authenticated_user = True


class RegisterUserView(views.CreateView):
    template_name = "accounts/register-page.html"
    form_class = PetstagramUserCreationForm
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)

        return result


def signout_user(request):
    logout  (request)
    return redirect("home_page")


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects \
        .prefetch_related("user") \
        .all()

    template_name = "accounts/profile-details-page.html"


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/profile-edit-page.html"
    fields = ("first_name", "last_name", "date_of_birth", "profile_picture")

    def get_success_url(self):
        return reverse("details_profile", kwargs={
            "pk": self.object.pk,
        })


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/profile-delete-page.html"
