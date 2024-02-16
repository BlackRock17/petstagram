from django.shortcuts import render


def register_user(request):
    context = {}
    return render(request, template_name="accounts/register-page.html", context=context)


def signin_user(request):
    pass


def signout_user(request):
    pass


def details_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass