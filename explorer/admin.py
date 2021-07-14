from django.contrib import admin
from .models import Album, Artist, Song

class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",)
        }
    list_filter = ("album", "artist",)
    list_display = ("title", "album", "artist", "track_listing")

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("artist",)
    list_display = ("title", "artist")

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)