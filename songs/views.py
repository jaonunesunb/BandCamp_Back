from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from albums.models import Album
from .models import Song
from .serializers import SongSerializer


class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        album = get_object_or_404(Album, pk=pk)
        return Song.objects.filter(album=album)

    def perform_create(self, serializer):
        album = Album.objects.get(id= self.kwargs['pk'])
        serializer.save(album=album)
