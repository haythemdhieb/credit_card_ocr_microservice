import uuid

from fastapi import HTTPException
from numpy import ndarray

from pipeline_modules.classification_module.classification_pipeline import predict_image_class
from pipeline_modules.ocr_module.ocr import OcrPipeline

OcrPipeline = OcrPipeline()


def predict_file(file_id: uuid, user_id: uuid, image: ndarray) -> list:
    """
    Returns the result of the hole pipeline on the credit card
    Parameters:
        file_id(str)
        user_id(str)
        image(PIL image)
    Returns:
        detected text(list): list containing detected text
    """
    image_class = predict_image_class(image)
    if image_class == "other":
        raise HTTPException(status_code=406, detail="This is not a credit card")
    detected_text = OcrPipeline.main(image)
    return detected_text
