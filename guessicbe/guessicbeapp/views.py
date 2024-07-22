from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, World!")


def search_artist_by_name(request):
    artist_name = request.GET.get('name', '')
    return HttpResponse(f"I'll search for an artist by name: {artist_name}")
