from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import PetPhoto


class PetPhotoCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("tagged_pets")

    form_class = PetPhotoCreateForm
    template_name = "photos/photo-add-page.html"

    def get_success_url(self):
        return reverse("details_photo", kwargs={"pk": self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class PetPhotoDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("photolike_set") \
        .prefetch_related("photocomment_set") \
        .prefetch_related("tagged_pets")

    template_name = "photos/photo-details-page.html"


class PetPhotoEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("tagged_pets")

    form_class = PetPhotoEditForm
    template_name = "photos/photo-edit-page.html"

    def get_success_url(self):
        return reverse("details_photo", kwargs={"pk": self.object.pk})




