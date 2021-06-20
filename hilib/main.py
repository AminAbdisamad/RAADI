from fastapi import FastAPI
import uvicorn
from config import APP_NAME, DESCRIPTION, VERSION

app = FastAPI(title=APP_NAME, description=DESCRIPTION, version=VERSION)


@app.get("/")
def index():
    return {"name": "RAADI", "description": "Raadi api", "version": "0.0.1"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)


# Did some changes to the file
# Did some changes from Kayse