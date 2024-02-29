from django.urls import path

from petstagram.common.views import home_page, like_pet_photo

urlpatterns = (
    path("", home_page, name="home_page"),
    path("pet_photo_like/<int:pk>/", like_pet_photo, name="like_pet_photo"),
)
