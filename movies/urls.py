from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list),
    path('<int:movie_pk>/like/', views.movie_like),
]