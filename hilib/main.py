from fastapi import FastAPI
import uvicorn
from config import APP_NAME, DESCRIPTION, VERSION
from users.view import users
from Institutions.view import institutions


app = FastAPI(title=APP_NAME, description=DESCRIPTION, version=VERSION)
app.include_router(users)
app.include_router(institutions)


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
