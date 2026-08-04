import os 
import numpy as numpy 
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

file = 'season-2526.csv'
file_path = os.path.join(file)
df = pd.read_csv(file_path)

df.head()
print(df.shape)

newdf = df.copy()
df.rename(columns={"HomeTeam":"Team", "AwayTeam":"Opponent", "FTHG":"GoalsFor", "FTAG":"GoalsAgainst"}, inplace=True)
df["Venue"] = "Home" #Changing column names to prepare for concat and adding a new column 

newdf.rename(columns={ "AwayTeam": "Team", "HomeTeam": "Opponent", "FTHG": "GoalsAgainst", "FTAG":"GoalsFor"}, inplace=True)
newdf["Venue"] = "Away"
attempt = [df,newdf]
result = pd.concat(attempt)
result.to_csv("Season-2526Updated.csv", index = False)
results.tosql()