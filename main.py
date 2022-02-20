from imp import reload
from fastapi import FastAPI
from uvicorn import Server, Config
from routes import information_extraction
from configurations.config import CreCardSettings
import uvicorn

app = FastAPI()
app.include_router(information_extraction.router)


if __name__ == "__main__":
    uvicorn.run(app, host=CreCardSettings.HOST, port=CreCardSettings.PORT)