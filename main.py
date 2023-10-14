import time
from fastapi import FastAPI
from .models import Base
from .db import engine
import psycopg2
from psycopg2.extras import RealDictCursor
from .routes import contacts, states, countries

app = FastAPI()
app.include_router(contacts.router)
app.include_router(countries.router)
app.include_router(states.router)


Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg2.connect("dbname=ContactApplication user=postgres")
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        break
    except Exception as err:
        print("Could not establish connection to DB")
        print("Error: ", err)
        time.sleep(2)
