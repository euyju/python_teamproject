import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_class_labels(train_dir='data/train'):
    temp_gen = ImageDataGenerator(rescale=1./255)
    temp_data = temp_gen.flow_from_directory(
        train_dir,
        target_size=(128, 128),
        batch_size=1,
        class_mode='categorical',
        shuffle=False
    )
    class_indices = temp_data.class_indices
    class_labels = [None] * len(class_indices)
    for label, idx in class_indices.items():
        class_labels[idx] = label
    return class_labels

def predict_food(img_path):
    print("이미지를 분석하여 음식을 예측합니다...")
    model = tf.keras.models.load_model('food_model.h5')
    class_labels = load_class_labels()

    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    pred_index = np.argmax(pred)
    pred_class = class_labels[pred_index]

    print(f"✅ 예측 결과: {pred_class}")
    return pred_class