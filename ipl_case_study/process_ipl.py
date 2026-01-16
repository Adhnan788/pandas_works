import pandas as pd

df = pd.read_csv("ipl_case_study\ipl_data.csv")
print(df)
print(df.shape)
print(df.columns)

print(df.isnull().sum())

print(df.info())

print(df["match_id"].fillna(549,inplace=True))
print(df["season"].fillna(df["season"].mode()[0],inplace=True))
print(df["city"].fillna(df["city"].mode()[0],inplace=True))
print(df["team1"].fillna("unknown",inplace=True))
print(df["team2"].fillna("unknown",inplace=True))
print(df["winning_team"].fillna("unknown",inplace=True))
print(df["player_of_match"].fillna("unknown",inplace=True))
print(df["venue"].fillna(df["venue"].mode()[0],inplace=True))



run_round=round(df["runs_scored"].mean())
df["runs_scored"].fillna(run_round,inplace=True)

wickets_round=round(df["wickets"].mean())
df["wickets"].fillna(wickets_round,inplace=True)

print(df.isnull().sum())

print("matches per season",df["season"].value_counts())

#top match count season
print("top match count season ",df["season"].value_counts().idxmax())

#total match won by each team
print("total match won by each team",df["winning_team"].value_counts())

#avg runs per team
print("avg runs per team",df.groupby("season")["runs_scored"].mean())

#venue wise match count
print("venue wise match count",df["venue"].value_counts())

# venue wise avg runs
print("venue wise avg runs",df.groupby("venue")["runs_scored"].mean())

#city wise
print("city wise match count",df["city"].value_counts())

# city wise
print("city wise avg runs",df.groupby("city")["runs_scored"].mean())


#which team has highest run by winning team

print("which team has highest run by winning team",df.groupby("winning_team")["runs_scored"].mean().idxmax())

#highest top venue
print("highest top 3 venue",df["venue"].value_counts().head(3))