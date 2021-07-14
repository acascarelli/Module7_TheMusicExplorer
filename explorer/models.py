from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    web_site = models.URLField(max_length=200, null=True, blank=True)    
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("artist-detail", args=[self.slug])

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("album-detail", args=[self.slug])
    
    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(default="", null=False, db_index=True)
    track_listing = models.IntegerField(validators=[MinValueValidator(1)], null=True)

    def get_absolute_url(self):
        return reverse("song-detail", args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['track_listing']
