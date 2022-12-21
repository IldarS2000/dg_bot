from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.applications.xception import Xception
from keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image

from config import DESC_MODEL_PATH, TOKENIZER_PATH


def generate_desc(model, tokenizer, photo, max_length):
    in_text = ''
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        predicted = model.predict([photo, sequence], verbose=0)
        predicted = np.argmax(predicted)
        word = word_for_id(predicted, tokenizer)
        if word is None or word == 'end':
            break
        in_text += ' ' + word
    return in_text


def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None


def extract_features(filename, model):
    try:
        image = Image.open(filename)
    except Exception:
        print("ERROR: Couldn't open image! Make sure the image path and extension is correct")
        return

    image = image.resize((299, 299))
    image = np.array(image)
    # for images that has 4 channels, we convert them into 3 channels
    if image.shape[2] == 4:
        image = image[..., :3]
    image = np.expand_dims(image, axis=0)
    image = image / 127.5
    image = image - 1.0
    feature = model.predict(image)
    return feature


class DescriptionGenerator:
    def __init__(self):
        self.tokenizer = load(open(TOKENIZER_PATH, "rb"))
        self.model = load_model(DESC_MODEL_PATH)
        self.xception_model = Xception(include_top=False, pooling="avg")

    def generate_description(self, image_path):
        photo = extract_features(image_path, self.xception_model)
        description = generate_desc(self.model, self.tokenizer, photo, 32)
        return description


DESCRIPTION_GENERATOR = DescriptionGenerator()
