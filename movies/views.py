from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie
from movies import serializers

def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)