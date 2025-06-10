# main.py
from fastapi import FastAPI
from routes import booking

app = FastAPI()
app.include_router(booking.router)



