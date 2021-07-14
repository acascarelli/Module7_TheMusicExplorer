from django.shortcuts import render
from django.views import generic
from .models import Artist, Album, Song

# Create your views here.
def starting_page(request):
    return render(request, "explorer/index.html")

class all_artists(generic.ListView):
   model = Artist
   context_object_name = 'artists'

class all_albums(generic.ListView):
   model = Album
   context_object_name = 'albums'

def all_songs(request):
   context = {}
   context["songs"] = Song.objects.all().order_by("artist", "album", "track_listing")
   context["albums"] = Album.objects.all()
   return render(request, "explorer/song_list.html", context)

def artist_detail(request, slug):
   found_artist = Artist.objects.get(slug=slug)
   albums = Album.objects.filter(artist=found_artist)
   return render(request, "explorer/artist_detail.html", {
      "artist": found_artist,
      "albums": albums
   })

def album_detail(request, slug):
   found_album= Album.objects.get(slug=slug)
   songs = Song.objects.filter(album=found_album)
   return render(request, "explorer/album_detail.html", {
      "album": found_album,
      "songs": songs
   })

def song_detail(request, slug):
   found_song = Song.objects.get(slug=slug)
   return render(request, "explorer/song_detail.html", {
      "song": found_song
   })

def manage_music(request):
   return render(request, "explorer/manage_music.html")
