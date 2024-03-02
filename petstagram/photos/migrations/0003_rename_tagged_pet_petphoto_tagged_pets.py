from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0002_alter_petphoto_photo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="petphoto",
            old_name="tagged_pet",
            new_name="tagged_pets",
        ),
    ]