# Generated by Django 5.0 on 2024-01-29 15:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("album", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Albums",
            new_name="Album",
        ),
    ]