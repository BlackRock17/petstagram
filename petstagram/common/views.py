from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


def home_page(request):
    context = {
        "pet_photos": PetPhoto.objects.all()
    }
    return render(request, template_name="common/home-page.html", context=context)


def like_pet_photo(request, pk):
    # pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo_like = PhotoLike.objects.filter(to_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(to_photo_id=pk)

    return redirect(request.META.get("HTTP_REFERER") + f"#photo-{pk}")
