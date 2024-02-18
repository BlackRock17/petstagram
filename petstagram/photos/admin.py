from django.contrib import admin

from petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ("pk", "location", "date_of_publication", "short_description", "tagged_pets",)

    def short_description(self, obj):
        return obj.description[:15]

    def tagged_pets(self, obj):
        return ", ".join(pet.name for pet in obj.pets.all())
