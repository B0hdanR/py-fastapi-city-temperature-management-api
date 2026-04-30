from fastapi import FastAPI

from app.database import Base, engine
import app.models
from app.routers import city, temperature

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(city.router)
app.include_router(temperature.router)
