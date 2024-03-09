from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet
from django.contrib.auth import mixins as auth_mixin


class PetCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    # model = Pet
    template_name = "pets/pet-add-page.html"
    form_class = PetCreateForm

    def get_success_url(self):
        return reverse("details_pet", kwargs={
            "username": "lyubo",
            "pet_slug": self.object.slug,
        })

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.user = self.request.user
    #     return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class PetDetailView(auth_mixin.LoginRequiredMixin, views.DetailView):

    queryset = Pet.objects.all() \
        .prefetch_related("petphoto_set") \
        .prefetch_related("petphoto_set__photolike_set") \
        .prefetch_related("petphoto_set__tagged_pets")

    template_name = "pets/pet-details-page.html"
    slug_url_kwarg = "pet_slug"


class PetEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = "pets/pet-edit-page.html"
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "lyubo"
        return context

    def get_success_url(self):
        return reverse("details_pet", kwargs={
            "username": self.request.GET.get("username"),
            "pet_slug": self.object.slug,
        })


# def delete_pet(request, username, pet_slug):
#
#     pet = Pet.objects.filter(slug=pet_slug).get()
#     form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         form.save()
#         return redirect("home_page")
#
#     context = {
#         "pet_form": form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, template_name="pets/pet-delete-page.html", context=context)

class PetDeleteView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Pet
    template_name = "pets/pet-delete-page.html"
    form_class = PetDeleteForm
    success_url = reverse_lazy("home_page")
    slug_url_kwarg = "pet_slug"

    extra_context = {
        "username": "lyubo",
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    # THE SAME SOLUTION LIKE get_form_kwargs
    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #
    #     form = self.form_class(instance=self.object)
    #
    #     context["form"] = form
    #
    #     return context
