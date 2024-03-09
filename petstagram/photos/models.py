from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, BaseValidator
from django.db import models

from petstagram.pets.models import Pet
UserModel = get_user_model()


class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return max_size < file_size


class PetPhoto(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    MAX_LOCATION_LENGTH = 30

    MAX_PHOTO_SIZE = 5 * 1024 * 1024

    photo = models.ImageField(
        upload_to="pet_photos/",
        null=False,
        blank=False,
        validators=(MaxFileSizeValidator(limit_value=MAX_PHOTO_SIZE,),),
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),)
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    user = models.ForeignKey(UserModel,
                             on_delete=models.RESTRICT)