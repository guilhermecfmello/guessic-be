from django.urls import path

from guessicbeapp.views import search_artist_by_name

urlpatterns = [
    path('artist/search', search_artist_by_name)
]
