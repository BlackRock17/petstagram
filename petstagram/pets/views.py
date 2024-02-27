from django.shortcuts import render

from petstagram.pets.models import Pet


def add_pet(request):
    context = {}
    return render(request, template_name="pets/pet-add-page.html", context=context)


def details_pet(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug)
    }
    return render(request, template_name="pets/pet-details-page.html", context=context)


def edit_pet(request, username, pet_slug):
    context = {}
    return render(request, template_name="pets/pet-edit-page.html", context=context)


def delete_pet(request, username, pet_slug):
    context = {}
    return render(request, template_name="pets/pet-delete-page.html", context=context)