"""
joins in pandas
combine multiple dataframes based on a column
"""

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
    {"id": 10, "movie_id": 6, "message": "The teaser looks promising, can't wait for Yash!", "rating": 4.5, "owner": "yash_army"},
    {"id": 11, "movie_id": 3, "message": "Too long for my taste, though visuals were stunning.", "rating": 3.5, "owner": "mark_robert"},
    {"id": 12, "movie_id": 1, "message": "Storytelling at its best. Malayalam cinema is peaked.", "rating": 4.7, "owner": "sree_mallu"},
    {"id": 13, "movie_id": 5, "message": "Some jokes felt repetitive, but the climax saved it.", "rating": 3.8, "owner": "rohit_verma"},
    {"id": 14, "movie_id": 7, "message": "Average plot, but the music was catchy.", "rating": 3.0, "owner": "sneha_j"},
    {"id": 15, "movie_id": 1, "message": "A bit overhyped but still a solid entertainer.", "rating": 3.5, "owner": "faisal_khan"},
    {"id": 16, "movie_id": 2, "message": "Prabhas is back with a bang! Epic visuals.", "rating": 4.5, "owner": "telugu_talkies"},
    {"id": 17, "movie_id": 4, "message": "The emotion in this movie is so real. I cried.", "rating": 5.0, "owner": "meera_nair"},
    {"id": 18, "movie_id": 3, "message": "Hans Zimmer score is the soul of this film.", "rating": 5.0, "owner": "music_buff"},
    {"id": 19, "movie_id": 6, "message": "The wait for 2025 is going to be long.", "rating": 4.0, "owner": "rockybhai_fan"},
    {"id": 20, "movie_id": 1, "message": "Incredible production quality for a regional film.", "rating": 4.2, "owner": "arjun_v"},
    {"id": 21, "movie_id": 2, "message": "Amitabh Bachchan stole the show as Ashwatthama.", "rating": 4.8, "owner": "bollywood_lover"},
    {"id": 22, "movie_id": 5, "message": "Shraddha and Rajkumar Rao chemistry is gold.", "rating": 4.5, "owner": "desi_critic"},
    {"id": 23, "movie_id": 7, "message": "The de-aging tech was hit and miss for me.", "rating": 2.5, "owner": "tech_guru"},
    {"id": 24, "movie_id": 3, "message": "The scale of this movie is just massive.", "rating": 4.0, "owner": "imax_only"},
    {"id": 25, "movie_id": 4, "message": "Realism at its finest. Proud of Malayalam films.", "rating": 4.9, "owner": "kerala_vibes"},
    {"id": 26, "movie_id": 1, "message": "Could have been edited better in the second half.", "rating": 3.0, "owner": "editor_eye"},
    {"id": 27, "movie_id": 2, "message": "The cameos were the best part of the movie!", "rating": 4.2, "owner": "fan_theory"},
    {"id": 28, "movie_id": 5, "message": "The horror elements were actually scary this time.", "rating": 4.0, "owner": "ghost_hunter"},
    {"id": 29, "movie_id": 7, "message": "Thalapathy Vijay screen presence is unmatched.", "rating": 4.5, "owner": "vijay_merasal"},
    {"id": 30, "movie_id": 3, "message": "Didn't like the ending compared to the book.", "rating": 3.0, "owner": "bookworm_01"},
    {"id": 31, "movie_id": 1, "message": "Tovino has truly evolved as an actor.", "rating": 4.6, "owner": "film_buff_07"},
    {"id": 32, "movie_id": 2, "message": "Science fiction meets mythology perfectly.", "rating": 4.5, "owner": "myth_nerd"},
    {"id": 33, "movie_id": 4, "message": "What a nail-biting experience. Don't miss it.", "rating": 4.7, "owner": "thrill_seeker"},
    {"id": 34, "movie_id": 6, "message": "Neel + Yash = Explosive combo.", "rating": 4.8, "owner": "karnataka_cinema"},
    {"id": 35, "movie_id": 5, "message": "Laughed after a very long time in a theater.", "rating": 4.4, "owner": "jolly_p"},
    {"id": 36, "movie_id": 1, "message": "The cinematography is like a painting.", "rating": 4.8, "owner": "camera_guy"},
    {"id": 37, "movie_id": 3, "message": "A bit too philosophical for an action movie.", "rating": 3.5, "owner": "john_doe"},
    {"id": 38, "movie_id": 7, "message": "The climax twist was totally unexpected!", "rating": 4.0, "owner": "twist_lover"},
    {"id": 39, "movie_id": 2, "message": "BGM was too loud in some scenes.", "rating": 3.5, "owner": "sound_checker"},
    {"id": 40, "movie_id": 4, "message": "Friendship goals! Highly emotional.", "rating": 5.0, "owner": "besties_3"},
    {"id": 41, "movie_id": 5, "message": "Pankaj Tripathi is a legend. Pure comedy.", "rating": 4.6, "owner": "mirzapur_fan"},
    {"id": 42, "movie_id": 1, "message": "The mythology aspect was handled very well.", "rating": 4.3, "owner": "history_geek"},
    {"id": 43, "movie_id": 7, "message": "Expected more from the director's track record.", "rating": 2.8, "owner": "strict_critic"},
    {"id": 44, "movie_id": 2, "message": "Best VFX ever seen in Indian cinema history.", "rating": 5.0, "owner": "vfx_artist"},
    {"id": 45, "movie_id": 3, "message": "A must watch on the biggest screen possible.", "rating": 4.5, "owner": "screen_junkie"},
    {"id": 46, "movie_id": 4, "message": "The casting was perfect for every character.", "rating": 4.7, "owner": "talent_scout"},
    {"id": 47, "movie_id": 6, "message": "Setting high expectations for this one.", "rating": 4.0, "owner": "sandalwood_king"},
    {"id": 48, "movie_id": 5, "message": "Great family entertainer for the weekend.", "rating": 4.2, "owner": "family_man"},
    {"id": 49, "movie_id": 1, "message": "Truly an international standard from Kerala.", "rating": 4.9, "owner": "global_malayali"},
    {"id": 50, "movie_id": 2, "message": "Can't wait for Part 2! That cliffhanger!", "rating": 4.6, "owner": "marv_fan"}
]

import pandas as pd

movies=pd.DataFrame(movies_data)
print(movies.columns)
print(movies.isnull().sum())


reviews=pd.DataFrame(reviews_data)
print(reviews.columns)
print(reviews.isnull().sum())

# merge

data=pd.merge(movies,reviews,left_on="id",right_on="movie_id",how="inner")
print(data.head(3))

print(data["title"].value_counts())

print(data.groupby("title")["rating"].mean())

#year_wise movies count

print(movies["year"].value_counts())

#language wise movie count

print(movies["language"].value_counts())

#language wise review count

print(data["language"].value_counts())

#language wise avg rating

print(data.groupby("language")["rating"].mean())