# Generated by Django 5.0 on 2024-02-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("album", "0002_rename_albums_album"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]
