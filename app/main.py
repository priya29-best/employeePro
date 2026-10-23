from fastapi import FastAPI
from .database import engine, Base
from .routers import employees
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Pro API - Day 4")

app.include_router(employees.router)

@app.get("/")
def root():
    return {"msg": "Day 4 Running - Routers Active, Main.py Clean!"}