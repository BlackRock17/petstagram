from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
from django.views import generic as views
from petstagram.accounts.forms import PetstagramUserCreationForm


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


def details_profile(request, pk):
    context = {}
    return render(request, template_name="accounts/profile-details-page.html", context=context)


def edit_profile(request, pk):
    context = {}
    return render(request, template_name="accounts/profile-edit-page.html", context=context)


def delete_profile(request, pk):
    context = {}
    return render(request, template_name="accounts/profile-delete-page.html", context=context)
