from django.shortcuts import render

from petstagram.photos.models import PetPhoto


def home_page(request):
    context = {
        "pet_photos": PetPhoto.objects.all()
    }
    return render(request, template_name="common/home-page.html", context=context)
