import uuid
from typing import Optional

from pydantic import BaseModel, Field


class FileForPrediction(BaseModel):
    file_id: uuid.UUID = Field(description="File ID",
                         example="567e6b52-e4fd-4262-8409-f8c75c8e777b")
    user_id: uuid.UUID = Field(
        description="user unique id",
        example="95e8b1c3-9254-446e-a151-dddb91c395eb")

class DetectedEntities(BaseModel):
    banck_name: str = ""
    first_name: str =""
    last_name: str=""
    credit_card_number: str = ""

class OutputModel(BaseModel):
    status: str = "processed"
    ocr_results: DetectedEntities 
    file_id: uuid.UUID = Field(description="File ID",
                         example="567e6b52-e4fd-4262-8409-f8c75c8e777b")
    user_id: uuid.UUID = Field(
        description="user unique",
        example="95e8b1c3-9254-446e-a151-dddb91c395eb")