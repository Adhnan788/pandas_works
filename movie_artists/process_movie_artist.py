import pandas as pd

df=pd.read_csv("movie_artists\movie_artist.csv")

print(df)
print(df.shape)
print(df.columns)

print(df.isnull().sum())

print(df.info())

#filter female actors
female_actors = df[df["gender"] == "Female"]
print(female_actors)

#filter male actors
male_actors=df[df["gender"]== "Male"]
print(male_actors)

#artist who is inactive
artists_inactive=df[df["active_status"]=="Inactive"]
print(artists_inactive)

#most awards by artists
most_awards = df[df["no_of_awards"] > 20]
print(most_awards)

#average gender age
avg_gender_age=df.groupby("gender")["age"].mean().round()
print(avg_gender_age)

#birth place = thrissur
thrissur_birth=df[df["place_of_birth"] == "Thrissur"]
print(thrissur_birth)
