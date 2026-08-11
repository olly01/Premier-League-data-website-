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
    "https://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins =origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers =["*"],
)


@app.get("/")
def root():
    return {"message": car}



def csvToSQL():
    df = pd.read_csv('./csv/Season-2526Updated.csv')
    
    db = sqlite3.connect('Premierleague_table.db')
    cursor = db.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS table_2526(GameID INTEGER Primary Key, Date TEXT, Team TEXT, Opponent TEXT, GoalsFor INT, GoalsAgainst INT, FTR INT, HTHG INT, HTAG INT, HTR INT, Referee TEXT, HS INT, [AS] INT, HST INT, AST INT, HF INT, AF INT, HC INT, AC INT, HY INT, AY INT, HR INT, AR INT, Venue TEXT);")
    print(cursor.execute("SELECT * FROM table_2526 ;"))
    for row in df.itertuples(index=False):
            cursor.execute("INSERT INTO table_2526(Date, Team, Opponent, GoalsFor, GoalsAgainst, FTR, HTHG, HTAG, HTR, Referee, HS, [AS], HST, AST, HF, AF, HC, AC, HY, AY, HR, AR, Venue) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
    db.commit()
    self = cursor.execute("SELECT * FROM table_2526 ;")
    print(self.fetchone())

if __name__ == "__main__":
    csvToSQL()
   # uvicorn.run(app, host="0.0.0.0", port=8000)