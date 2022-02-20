from io import BytesIO

import numpy as np
from fastapi import APIRouter, Depends, File, UploadFile
from loguru import logger
from PIL import Image
from data_schemas.models import FileForPrediction
from pipeline_modules.prediction_pipeline import predict_file

router = APIRouter()


@router.post("/predict_file", name="prediction")
async def prediction(data: FileForPrediction = Depends(), file: UploadFile = File(...)):
    """
    Prediction endpoint
    """
    image = Image.open(BytesIO(file.file.read())).convert("RGB")
    return predict_file(data.file_id, data.user_id, np.array(image))