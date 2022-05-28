from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    # genre = models.ManyToManyField(
    #     Genre,
    #     related_name='genre_movies'
    # )
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.pk}번 영화: {self.title}'

    





