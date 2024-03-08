from django.urls import path, include

from petstagram.photos.views import PetPhotoCreateView, PetPhotoDetailsView, PetPhotoEditView

urlpatterns = (
    path("add/", PetPhotoCreateView.as_view(), name="add_photo"),
    path("<int:pk>/", include([
        path("", PetPhotoDetailsView.as_view(), name="details_photo"),
        path("edit/", PetPhotoEditView.as_view(), name="edit_photo"),
    ]))
)
