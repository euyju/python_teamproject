import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from FoodAPI import get_nutrition_info
import os

# 모델 로드
model = tf.keras.models.load_model('food_model.h5')

# 클래스 라벨 (예시)
class_labels = ['apple_pie', 'bibimbap', 'pizza', 'ramen']

# 테스트 이미지 경로
img_path = './test_images/test.jpg'

# 이미지 전처리
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# 예측
pred = model.predict(img_array)
pred_index = np.argmax(pred)
pred_class = class_labels[pred_index]

print(f"🔍 예측 음식: {pred_class}")
get_nutrition_info(pred_class)