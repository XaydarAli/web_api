from django.shortcuts import render

from django.views import View
import requests


class HomeView(View):
    def get(self, request):
        artists=requests.get("http://localhost:8000/artists").json()
        context={'artists':artists}
        return render(request, 'home.html',context)

class ArtistView(View):
    def get(self, request):
        artists = requests.get("http://localhost:8000/artists").json()
        context = {'artists': artists}
        return render(request, 'artists.html',context)

class SongView(View):
    def get(self, request):
        songs=requests.get("http://localhost:8000/songs").json()
        context={'songs':songs}
        return render(request, 'songs.html',context)

class AlbumView(View):
    def get(self, request):
        albums=requests.get("http://localhost:8000/albums").json()
        context={'albums':albums}
        return render(request, 'albums.html',context)
