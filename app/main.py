<<<<<<< HEAD
import mysql.connector
import os
from mysql.connector import Error
from fastapi import FastAPI

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "esd4uq"
=======
#!/usr/bin/env python3

import json
import os
from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error
>>>>>>> faaf7b6123dda43b76098885671bb7a833f95988

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "nem2p"

def read_root():
    return {"message": "Hello, FastAPI!"}

<<<<<<< HEAD
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/genres')
def get_genres():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
    cur=db.cursor()
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
=======
@app.get('/genres')
async def get_genres():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB, ssl_disabled=True)
    cur = db.cursor()
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        print("MySQL Error: ", str(e))
        return {"Error": "MySQL Error: " + str(e)}
    finally:
        cur.close()
        db.close()

@app.get('/songs')
async def get_genres():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB, ssl_disabled=True)
    cur = db.cursor()
    query = "SELECT songs.title, songs.album, songs.artist, songs.year, songs.file, songs.image, genres.genre FROM songs JOIN genres WHERE songs.genre = genres.genreid;"
    try:
>>>>>>> faaf7b6123dda43b76098885671bb7a833f95988
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
<<<<<<< HEAD
        cur.close()
        db.close()
        return(json_data)
    except Error as e:
        cur.close()
        db.close()
        return {"Error": "MySQL Error: " + str(e)}
    
@app.get('/songs')
def get_songs():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
    cur=db.cursor()
    query = """
    SELECT 
        songs.title AS title, 
        songs.album AS album, 
        songs.artist AS artist, 
        songs.year AS year, 
        songs.file AS file, 
        songs.image AS image,
        genres.genre AS genre
    FROM 
        songs
    JOIN 
        genres ON songs.genre = genres.genreid
    ORDER BY
        songs.title;
    """
    try:
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = [dict(zip(headers, result)) for result in results]
        cur.close()
        db.close()
        return json_data
    except mysql.connector.Error as e:
        cur.close()
        db.close()
        return {"Error": "Failed to fetch songs"}
=======
        return(json_data)
    except Error as e:
        print("MySQL Error: ", str(e))
        return None
    finally:
        cur.close()
        db.close()
>>>>>>> faaf7b6123dda43b76098885671bb7a833f95988
