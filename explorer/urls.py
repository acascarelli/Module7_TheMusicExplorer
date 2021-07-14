from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name="starting_page"),
    path('artists', views.all_artists.as_view(), name="artist_list"),
    path('albums', views.all_albums.as_view(), name="album_list"),
    path('songs', views.all_songs, name="song_list"),
    path('artists/<slug:slug>', views.artist_detail, name="artist_detail_page"),
    path('album/<slug:slug>', views.album_detail, name="album_detail_page"),
    path('songs/<slug:slug>', views.song_detail, name="song_detail_page"),
    path('manage-music', views.manage_music, name="manage_music")
]