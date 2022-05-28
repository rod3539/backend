from django.db import models
from movies.models import Movie


class Recommend(models.Model):
    title = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=200)
    overview = models.TextField()
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='recommend_movie'
    )