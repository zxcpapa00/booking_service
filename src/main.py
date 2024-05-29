from fastapi import FastAPI
from src.routers.users import router as users_router
from src.routers.hotels import router as hotels_router

app = FastAPI()
app.include_router(users_router)
app.include_router(hotels_router)
