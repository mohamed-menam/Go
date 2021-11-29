from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
import movie

from movie.admin import MovieAdmin
from movie.models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, "movie/index.html", {"movies": movies})


def indcook(request):
    movies = Movie.objects.all()
    output = ", ".join([m.title for m in movies])
    return HttpResponse(output)


def flliter(request):
    return HttpResponse(Movie.objects.filter(release_year=2005))

# movies = Movie.get_object_or_404(pk=movie_id)


def details(request, movie_id):
    try:
        movies = Movie.objects.get(pk=movie_id)
        return render(request, "movie/details.html", {"movies": movies})
    except Movie.DoesNotExist:
        raise Http404()
