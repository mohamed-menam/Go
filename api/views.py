from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import MovieSerializers, GenerSerializers
from movie.models import Movie, Genre
# Create your views here.


class MovieViewsets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class GenerViewsets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenerSerializers


def logout_view(request):
    logout(request)
