from django.http import JsonResponse
from rest_framework import status

from guessicbeapp.models import Artist


def search_artist_by_name(request):
    artist_name = request.GET.get('name', '')
    artists = Artist.objects.filter(name__icontains=artist_name)

    response_data = [
        {"id": str(artist.id), "name": artist.name} for artist in artists
    ]

    return JsonResponse(response_data, safe=False, status=status.HTTP_200_OK)
