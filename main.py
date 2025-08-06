from fastapi import FastAPI
from routes.time_off import router as time_off_router

app = FastAPI(title="Time Off API", version="1.0.0")

app.include_router(time_off_router)
