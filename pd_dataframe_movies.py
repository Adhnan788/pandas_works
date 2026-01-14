movies = [
    {"title": "The Shawshank Redemption", "language": "English", "year": 1994, "run_time": 142, "rating": 9.3, "collection": 28.3},
    {"title": "The Godfather", "language": "English", "year": 1972, "run_time": 175, "rating": 9.2, "collection": 246.1},
    {"title": "The Dark Knight", "language": "English", "year": 2008, "run_time": 152, "rating": 9.0, "collection": 1005.0},
    {"title": "Schindler's List", "language": "English", "year": 1993, "run_time": 195, "rating": 9.0, "collection": 322.2},
    {"title": "Pulp Fiction", "language": "English", "year": 1994, "run_time": 154, "rating": 8.9, "collection": 213.9},
    {"title": "Parasite", "language": "Korean", "year": 2019, "run_time": 132, "rating": 8.5, "collection": 263.1},
    {"title": "Spirited Away", "language": "Japanese", "year": 2001, "run_time": 125, "rating": 8.6, "collection": 355.7},
    {"title": "Inception", "language": "English", "year": 2010, "run_time": 148, "rating": 8.8, "collection": 836.8},
    {"title": "Seven Samurai", "language": "Japanese", "year": 1954, "run_time": 207, "rating": 8.6, "collection": 0.3},
    {"title": "Interstellar", "language": "English", "year": 2014, "run_time": 169, "rating": 8.7, "collection": 701.7},
    {"title": "The Matrix", "language": "English", "year": 1999, "run_time": 136, "rating": 8.7, "collection": 467.2},
    {"title": "City of God", "language": "Portuguese", "year": 2002, "run_time": 130, "rating": 8.6, "collection": 30.6},
    {"title": "RRR", "language": "Telugu", "year": 2022, "run_time": 187, "rating": 7.8, "collection": 160.0},
    {"title": "Life Is Beautiful", "language": "Italian", "year": 1997, "run_time": 116, "rating": 8.6, "collection": 230.1},
    {"title": "The Intouchables", "language": "French", "year": 2011, "run_time": 112, "rating": 8.5, "collection": 426.6},
    {"title": "Avengers: Endgame", "language": "English", "year": 2019, "run_time": 181, "rating": 8.4, "collection": 2797.0},
    {"title": "Dangal", "language": "Hindi", "year": 2016, "run_time": 161, "rating": 8.3, "collection": 311.0},
    {"title": "Coco", "language": "English", "year": 2017, "run_time": 105, "rating": 8.4, "collection": 807.8},
    {"title": "Your Name", "language": "Japanese", "year": 2016, "run_time": 106, "rating": 8.4, "collection": 382.2},
    {"title": "Joker", "language": "English", "year": 2019, "run_time": 122, "rating": 8.4, "collection": 1074.0},
    {"title": "Oldboy", "language": "Korean", "year": 2003, "run_time": 120, "rating": 8.4, "collection": 15.0},
    {"title": "Amélie", "language": "French", "year": 2001, "run_time": 122, "rating": 8.3, "collection": 174.1},
    {"title": "Toy Story", "language": "English", "year": 1995, "run_time": 81, "rating": 8.3, "collection": 373.6},
    {"title": "Inglourious Basterds", "language": "English", "year": 2009, "run_time": 153, "rating": 8.3, "collection": 321.4},
    {"title": "Good Will Hunting", "language": "English", "year": 1997, "run_time": 126, "rating": 8.3, "collection": 225.9},
    {"title": "The Hunt", "language": "Danish", "year": 2012, "run_time": 115, "rating": 8.3, "collection": 18.3},
    {"title": "A Separation", "language": "Persian", "year": 2011, "run_time": 123, "rating": 8.3, "collection": 22.9},
    {"title": "Mad Max: Fury Road", "language": "English", "year": 2015, "run_time": 120, "rating": 8.1, "collection": 380.4},
    {"title": "Django Unchained", "language": "English", "year": 2012, "run_time": 165, "rating": 8.5, "collection": 425.4},
    {"title": "The Grand Budapest Hotel", "language": "English", "year": 2014, "run_time": 99, "rating": 8.1, "collection": 173.0},
    # ... (Note: For brevity, listing key samples below. Total list continues in this pattern)
]

import pandas as pd

df=pd.DataFrame(movies)

print(df.shape)

print(df.columns)

print(df.head())

print(df.info())

print(df[["title","rating"]])

print(df[df["language"]=="English"])

print(df[df["rating"]>8][["title","rating"]])

print(df["run_time"].max())