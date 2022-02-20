from fastapi import FastAPI

from routes import information_extraction
import uvicorn
from configurations.config import CreCardSettings
app = FastAPI()
app.include_router(information_extraction.router)

if __name__ == "__main__":
    uvicorn.run(app, host=CreCardSettings.HOST, port=CreCardSettings.PORT)
