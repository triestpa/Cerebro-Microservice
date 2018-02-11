"""Classification Model Module"""
import sys
import requests
import numpy as np
from PIL import Image
from io import BytesIO
from keras.preprocessing import image

# from keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input, decode_predictions

TARGET_SIZE = (299, 299)
TOP_N = 3

class Classifier():
    """Classifier Model Wrapper Class"""

    def __init__(self):
        """Initialize the model with the specified weights"""
        self.model = InceptionResNetV2(weights='imagenet')

    def predict(self, img):
        """Predict the possible classes of the image"""

        # Resize image to InceptionV3 expected size
        if img.size != TARGET_SIZE:
            img = img.resize(TARGET_SIZE)

        # Preprocess image as Tensorflow model input
        input = image.img_to_array(img)
        input = np.expand_dims(input, axis=0)
        input = preprocess_input(input)

        # Predict classes
        preds = self.model.predict(input)

        # Format and return results
        preds = decode_predictions(preds, top=TOP_N)[0]
        results = list(map(lambda pred: {'label': pred[1], 'score': pred[2] * 100}, preds))
        return results

    def predict_url(self, url):
        """Download image and predict classes"""

        img = Image.open(requests.get(url, stream=True).raw)
        return self.predict(img)

if __name__ == '__main__':
    """Standalone classifier execution - expects image url as first argument"""
    print(Classifier().predict_url(sys.argv[1]))
