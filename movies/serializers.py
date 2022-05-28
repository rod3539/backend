from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Movie


User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'movie_id', )



class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = (
            'pk',
            'user',
            'title',
            'release_data',
            'popularity',
            'vote_count',
            'vote_average',
            'overview',
            'poster_path',
            'genre',
            'like_users',
        )