from django.urls import path, include

from petstagram.photos.views import add_photo, details_photo, edit_photo

urlpatterns = (
    path("add/", add_photo, name="add_photo"),
    path("<int:pk>/", include([
        path("", details_photo, name="details_photo"),
        path("edit/", edit_photo, name="edit_photo"),
    ]))
)
