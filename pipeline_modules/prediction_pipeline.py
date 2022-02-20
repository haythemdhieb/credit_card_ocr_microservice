from numpy import ndarray
from pipeline_modules.classification_module.classification_pipeline import predict_image_class

def predict_file(file_id:str,user_id:str,image:ndarray) -> str:
    """
    Returns the result of the hole pipeline on the credit card
    Parameters:
        filed_id: str
        user_id: str
        file : PIL image
    """
    image_class = predict_image_class(image)
    return image_class



