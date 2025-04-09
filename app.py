from fastapi import FastAPI
from app.routers import users, items
from app.database import database

app = FastAPI(title="Async FastAPI Example")

app.include_router(users.router, prefix="/api/v1")
app.include_router(items.router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Async FastAPI Demo"}