import cv2
import pytesseract
from numpy import ndarray

from utils.exceptions import CreditCardInvalid


class OcrPipeline:
    """
    Returns the detected text fields from the credit card
    """

    @staticmethod
    def process_image(image) -> ndarray:
        """
        :param image:  text extracted and cleaned from the business card
        :return: phone numbers extracted from business card
        """
        grayscaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresholded_image = cv2.threshold(grayscaled_image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        dilated_image = cv2.dilate(thresholded_image, kernel, iterations=1)
        return dilated_image

    @staticmethod
    def detect_countours_cv2(processed_image) -> list:
        """
        :param processed_image: extract text from dilated image
        :return: list of countours
        """
        contours, _ = cv2.findContours(processed_image, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)

        return contours

    @staticmethod
    def detect_text_from_image_cv2(contours, image):
        """
        :param contours: coutours from the image
        :param image: original business card image
        :return: list containing detected text
        """
        text = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped = image[y:y + h, x:x + w]
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imwrite("temp_image.png", image)
            text.append(pytesseract.image_to_string(cropped))

        return text

    def main(self, image) -> list:
        """
        :param image: business card image
        :return: list containing detected text
        """
        try:
            processed_image = self.process_image(image)
            contours = self.detect_countours_cv2(processed_image)
            detected_text = self.detect_text_from_image_cv2(contours, image)
        except Exception:
            raise CreditCardInvalid("error while processing this credit card")

        return detected_text
