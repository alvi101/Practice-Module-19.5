from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.IntegerField()
    img = models.ImageField(upload_to='uploads/', null=True, blank=True)

    musician = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name
