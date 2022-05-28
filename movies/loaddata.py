import requests
import json

# TMDB_API_KEY =   # .env 파일에서 불러옴.

def get_movie_datas():
    total_data = []

    for i in range(1, 20):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key=&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()


        for movie in movies['results']:
            if movie.get('release_date', ''):
                # fields = {
                    # 'movie_id': movie['id'],
                #     'title': movie['title'],
                #     'released_date': movie['release_date'],
                #     'popularity': movie['popularity'],
                #     'vote_avg': movie['vote_average'],
                #     'overview': movie['overview'],
                #     'poster_path': movie['poster_path'],
                #     'genres': movie['genre_ids']
                # }

                data = {
                    "model": "movies.movie",
                    "fields": {
                        'movie_id': movie['id'],
                        'title': movie['title'],
                        'release_date': movie['release_date'],
                        'popularity': movie['popularity'],
                        'vote_count': movie['vote_count'],
                        'vote_average': movie['vote_average'],
                        'overview': movie['overview'],
                        'poster_path': movie['poster_path'],
                    }
                }

                total_data.append(data)

    with open("movies.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=" ", ensure_ascii=False)

get_movie_datas()