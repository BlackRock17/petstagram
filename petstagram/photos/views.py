from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views

from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import PetPhoto


class PetPhotoCreateView(views.CreateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("tagged_pets")

    form_class = PetPhotoCreateForm
    template_name = "photos/photo-add-page.html"

    def get_success_url(self):
        return reverse("details_photo", kwargs={"pk": self.object.pk})


class PetPhotoDetailsView(views.DetailView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("photocomment_set") \
        .prefetch_related("tagged_pets")

    template_name = "photos/photo-details-page.html"


class PetPhotoEditView(views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("tagged_pets")

    form_class = PetPhotoEditForm
    template_name = "photos/photo-edit-page.html"

    def get_success_url(self):
        return reverse("details_photo", kwargs={"pk": self.object.pk})




