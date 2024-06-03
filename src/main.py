import uvicorn
from fastapi import FastAPI
from src.routers.users import router as users_router
from src.routers.hotels import router as hotels_router
from src.routers.rooms import router as rooms_router
from src.routers.bookings import router as bookings_router

app = FastAPI()
app.include_router(users_router)
app.include_router(hotels_router)
app.include_router(rooms_router)
app.include_router(bookings_router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=80, reload=True, log_level="info")

