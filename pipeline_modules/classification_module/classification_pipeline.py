from tensorflow.keras.models import load_model

classifier = load_model("pipeline_modules/classification_module/classification_model.h5")


def classification_module(image):
    image = image.reshape((1,) + image.shape)
    classification_result = classifier.predict(image)
    image_class = "credit card" if classification_result < 0.5 else "other"
    return image_class
