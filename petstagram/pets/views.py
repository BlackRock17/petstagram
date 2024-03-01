from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


def add_pet(request):

    pet_form = PetCreateForm(request.POST or None)

    if request.method == "POST":
        if pet_form.is_valid():
            created_pet = pet_form.save()
            return redirect("details_pet", username="lyubo", pet_slug=created_pet.slug)

    context = {
        "pet_form": pet_form,
    }

    return render(request, template_name="pets/pet-add-page.html", context=context)


def details_pet(request, username, pet_slug):

    context = {
        'pet': Pet.objects.get(slug=pet_slug)
    }

    return render(request, template_name="pets/pet-details-page.html", context=context)


def edit_pet(request, username, pet_slug):

    pet = Pet.objects.filter(slug=pet_slug).get()
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("details_pet", username=username, pet_slug=pet_slug)

    context = {
        "pet_form": form,
        "username": username,
        "pet": pet,
    }

    return render(request, template_name="pets/pet-edit-page.html", context=context)


def delete_pet(request, username, pet_slug):

    pet = Pet.objects.filter(slug=pet_slug).get()
    form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == "POST":
        form.save()
        return redirect("home_page")

    context = {
        "pet_form": form,
        "username": username,
        "pet": pet,
    }

    return render(request, template_name="pets/pet-delete-page.html", context=context)
