from django.urls import path, include

from petstagram.pets.views import PetCreateView, PetDetailView, PetEditView, PetDeleteView

urlpatterns = (
    path("add/", PetCreateView.as_view(), name="add_pet"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("", PetDetailView.as_view(), name="details_pet"),
        path("edit/", PetEditView.as_view(), name="edit_pet"),
        path("delete/", PetDeleteView.as_view(), name="delete_pet"),
    ]))
)
