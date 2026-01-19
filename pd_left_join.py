movies_data = [
    {"id": 1, "title": "ARM", "language": "Malayalam", "year": 2024},
    {"id": 2, "title": "Kalki 2898 AD", "language": "Telugu", "year": 2024},
    {"id": 3, "title": "Dune: Part Two", "language": "English", "year": 2024},
    {"id": 4, "title": "Manjummel Boys", "language": "Malayalam", "year": 2024},
    {"id": 5, "title": "Stree 2", "language": "Hindi", "year": 2024},
    {"id": 6, "title": "Toxic", "language": "Kannada", "year": 2025},
    {"id": 7, "title": "The Greatest of All Time", "language": "Tamil", "year": 2024}
]

reviews_data = [
    {"id": 1, "movie_id": 1, "message": "Must watch! Tovino's performance is top-notch.", "rating": 4.5, "owner": "vipin"},
    {"id": 2, "movie_id": 2, "message": "Visual spectacle, but the first half was a bit slow.", "rating": 4.0, "owner": "rahul_k"},
    {"id": 3, "movie_id": 3, "message": "A cinematic masterpiece. The sound design is incredible.", "rating": 5.0, "owner": "cinephile_99"},
    {"id": 4, "movie_id": 4, "message": "Heart-wrenching and beautifully shot. A survival gem.", "rating": 4.8, "owner": "amal_p"},
    {"id": 5, "movie_id": 5, "message": "Hilarious! Perfect sequel to the first one.", "rating": 4.2, "owner": "priya_sharma"},
    {"id": 6, "movie_id": 1, "message": "The 3D effects were actually good for a change.", "rating": 4.0, "owner": "deepu_v"},
    {"id": 7, "movie_id": 7, "message": "Pure fan service, but enjoyed the action sequences.", "rating": 3.5, "owner": "vijay_fan_boy"},
    {"id": 8, "movie_id": 2, "message": "Concept was great, but felt overstretched at 3 hours.", "rating": 3.0, "owner": "anita_review"},
    {"id": 9, "movie_id": 4, "message": "The background score gave me goosebumps.", "rating": 5.0, "owner": "karthik_007"},
    {"id": 10, "movie_id": 6, "message": "The teaser looks promising, can't wait for Yash!", "rating": 4.5, "owner": "yash_army"}
]

import pandas as pd

movies=pd.DataFrame(movies_data)
reviews=pd.DataFrame(reviews_data)
data=pd.merge(movies,reviews,left_on="id",right_on="movie_id",how="left")
print(data)