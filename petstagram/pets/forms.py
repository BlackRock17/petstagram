from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ("name", "date_of_birth", "pet_photo",)

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Pet name"}),
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "pet_photo": forms.URLInput(attrs={"placeholder": "Link to image"})
        }

        labels = {
            "name": "Pet name",
            "pet_photo": "Link to image"
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass
