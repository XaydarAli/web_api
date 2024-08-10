from django.urls import path
from .views import HomeView,ArtistView,AlbumView,SongView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artist/', ArtistView.as_view(), name='artist'),
    path('album/', AlbumView.as_view(), name='album'),
    path('song/', SongView.as_view(), name='song'),

]