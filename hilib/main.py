from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from config import APP_NAME, DESCRIPTION, VERSION
from users.view import users
from institutions.view import institutions
from reviews.views import reviews


app = FastAPI(title=APP_NAME, description=DESCRIPTION, version=VERSION)


origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users)
app.include_router(institutions)
app.include_router(reviews)


@app.get("/")
def index():
    return {"name": "RAADI", "description": "Raadi api", "version": "0.0.1"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)


# Users
# each section will have its own folder/directory
# that will contain models, service,view, util
# Insititutions
# Reviews
# Login/
# Database
# core databse instructions
