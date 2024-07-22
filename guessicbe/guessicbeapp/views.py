from django.http import HttpResponse
from rest_framework import status

from guessicbeapp.models import Artist


def search_artist_by_name(request):
    artist_name = request.GET.get('name', '')
    artists_found = Artist.objects.filter(name__icontains=artist_name)
    return HttpResponse(artists_found, content_type='application/json', status=status.HTTP_200_OK)
