from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Song
from .serializers import SongListSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all() 
        song_serializer = SongListSerializer(songs, many=True)
        return JsonResponse(song_serializer.data, safe=False)
 
    elif request.method == 'POST':
        song_data = JSONParser().parse(request)
        song_serializer = SongListSerializer(data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse(song_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Song.objects.all().delete()
        return JsonResponse({'message': '{} Songs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        song = Song.objects.get(pk=pk) 
    except song.DoesNotExist: 
        return JsonResponse({'message': 'The song does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        song_data = JSONParser().parse(request) 
        song_serializer = SongListSerializer(song, data=song_data) 
        if song_serializer.is_valid(): 
            song_serializer.save() 
            return JsonResponse(song_serializer.data) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        song.delete() 
        return JsonResponse({'message': 'Song was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)