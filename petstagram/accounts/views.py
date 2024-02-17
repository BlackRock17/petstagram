from django.shortcuts import render, redirect


def register_user(request):
    context = {}
    return render(request, template_name="accounts/register-page.html", context=context)


def signin_user(request):
    context = {}
    return render(request, template_name="accounts/login-page.html", context=context)


def signout_user(request):
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
