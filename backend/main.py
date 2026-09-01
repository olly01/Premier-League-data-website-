import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import sqlite3
import numpy as numpy 
import pandas as pd

table_dict = {
    "Date" : "TEXT",
    "Team" : "TEXT",
    "Opponent": "TEXT",
    "FTR" :"TEXT",
    "HTR" : "TEXT",
    "Referee" : "TEXT",
    "Venue" : "TEXT",
}

car = "hosue"
app = FastAPI()

origins = [
    "https://premierleaguedata.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins =origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers =["*"],
)
def dbconnect():
     db = sqlite3.connect('Premierleague_table.db')
     db.row_factory = sqlite3.Row
     cursor = db.cursor()
     return cursor

@app.get("/teamgoals/{team_name}")
def getGoals(team_name):
     team_name = team_name.capitalize()

@app.get("/allteams")
def getAllTeams():
     cursor = dbconnect()
     search = cursor.execute("SELECT DISTINCT Team FROM table_2526 ORDER BY Team ASC")
     result = [row[0] for row in search.fetchall()]
     return result



@app.get("/team/{team_name}")
def getTeam(team_name):
    
    db = sqlite3.connect('Premierleague_table.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
   
    search = cursor.execute("SELECT * FROM table_2526 WHERE Team = ? ORDER BY Date ASC",(team_name,) )
    result = search.fetchall()
    return result



def csvToSQL():
    df = pd.read_csv('./csv/Season-2526Updated.csv')
    db = sqlite3.connect('Premierleague_table.db')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS table_2526")
    db.commit()
    cursor.execute("CREATE TABLE IF NOT EXISTS table_2526(GameID INTEGER Primary Key, Date DATE, Team TEXT, Opponent TEXT, GoalsFor INT, GoalsAgainst INT, FTR INT, HTHG INT, HTAG INT, HTR INT, Referee TEXT, HS INT, [AS] INT, HST INT, AST INT, HF INT, AF INT, HC INT, AC INT, HY INT, AY INT, HR INT, AR INT, Venue TEXT);")
    for row in df.itertuples(index=False):
            cursor.execute("INSERT INTO table_2526(Date, Team, Opponent, GoalsFor, GoalsAgainst, FTR, HTHG, HTAG, HTR, Referee, HS, [AS], HST, AST, HF, AF, HC, AC, HY, AY, HR, AR, Venue) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
    db.commit()
    self = cursor.execute("SELECT DISTINCT Team FROM table_2526 WHERE Team LIKE '%Villa%' ")
    print("table check")
    print(self.fetchall())

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)