from email.policy import default
from functools import reduce
from typing import Any
import math

movies_ds = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# Этап 1

def average_rating(movies: list[dict[str, Any]]) -> float:
    return round(sum([movie["rating"] for movie in movies]) / len(movies))

def catalog_age_stats(movies: list[dict[str, Any]], current_year=2026) -> tuple[int, int, int]:
    movie_years = [movie["year"] for movie in movies]
    return (min(movie_years), max(movie_years), math.ceil(sum(movie_years) / len(movie_years)))

def duration_in_hours(minutes: int) -> str:
    return f'{minutes // 60}ч {minutes % 60}м'


# Этап 2

def rating_tier(rating: float) -> str:
    ratings = {
        9: "шедевр",
        7: "хорошо",
        5: "средне",
        0: "слабо"
    }
    return ratings.get(list(filter(lambda x: x <= rating, ratings))[0])


def decode_label(year: int) -> str:
    match year:
        case _ if year >= 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# Этап 3

def all_not_a_comedy(movies: list[dict[str, Any]]):
    for movie in movies:
        if list(filter(lambda x: x == "comedy", movie["genres"])):
            continue
        print(movie["title"])

def first_of_the_top(movies: list[dict[str, Any]]) -> str:
    i = 0
    while True:
        if movies[i]["rating"] > 9.0:
            return movies[i]["title"]
        i+=1
        if i >= len(movies):
            break
    return "Шедевров не найдено"

def count_long_movies(movies: list[dict[str, Any]], threshold=120) -> int:
    counter = 0
    for movie in movies:
        if movie["duration_min"] > 120:
            counter+=1
    return counter


# Этап 4

import operator


def normalize_title(title: str) -> str:
    words = title.split()
    i = 0
    while i < len(words):
        word = words[i]
        words[i] = word[0].upper() + word[1:].lower()
        i += 1
    return " ".join(words)


def make_slug(title: str) -> str:
    new_string = ""
    for char in title:
        if char == " ":
            new_string += "-"
        else:
            new_string += char.lower()
    return new_string


def format_report_line(movie: dict[str, Any]) -> str:
    genres = ", ".join(movie["genres"])
    return (
        f'{movie["title"]} ({movie["year"]}) - {movie["rating"]}/10 '
        f'{duration_in_hours(movie["duration_min"])}, жанры: {genres}'
    )


# Этап 5

def titles_sorted_by_rating(movies: list[dict[str, Any]]) -> list[str]:
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies: list[dict[str, Any]], n=3) -> list[tuple[str, int]]:
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


# Этап 6

def count_by_genre(movies: list[dict[str, Any]]) -> dict[str, int]:
    dict = {}
    for movie in movies:
        for genres in movie["genres"]:
            if dict.get(genres, False):
                dict[genres] += 1
            else:
                dict[genres] = 1
    return dict


def actor_filmography(movies: list[dict[str, Any]]) -> dict[str, int]:
    dict = {}
    for movie in movies:
        for actor in movie["actors"]:
            if dict.get(actor, False):
                dict[actor].append(movie["title"])
            else:
                dict[actor] = [movie["title"]]
    return dict

def title_above_average_rating(movies: list[dict[str, Any]]) -> dict[str, int]:
    rated_movies = list(filter(lambda x: x["rating"] > average_rating(movies), movies))
    return {movie["title"]: movie["rating"] for movie in rated_movies}

def all_genres(movies: list[dict[str, Any]]) -> set[str]:
    film_genres_set = set()
    for movie in movies:
        film_genres_set = film_genres_set | set([genre for genre in movie["genres"]])
    return film_genres_set

def common_actors(movie1: dict[str, Any], movie2: dict[str, Any]) -> set[str]:
    return set([actor for actor in movie1["actors"]]) & set([actor for actor in movie2["actors"]])

if __name__ == "__main__":
    print(common_actors(movies_ds[0], movies_ds[3]))

 
 