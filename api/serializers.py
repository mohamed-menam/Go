from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from movie.models import Movie, Genre


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
