from django.urls import path

from guessicbeapp.views import hello_world, search_artist_by_name

urlpatterns = [
    path('hello/', hello_world),
    path('artist/search', search_artist_by_name)
]
