import logging
import os

from pydantic import BaseModel, BaseSettings, Field


class CreCardSettings(BaseSettings):

    HOST: str = Field(default="localhost",
                      description="the host of the application ", env='HOST'
                      )
    PORT: str = Field(default="8009",
                      description="the port on whcih the application will run "
                      "weights ", env='PORT'
                      )


CreCardSettings = CreCardSettings()
