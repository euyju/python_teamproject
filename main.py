import os
from pathlib import Path
import subprocess
from FoodAPI import get_nutrition_info
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

def split_data_if_needed():
    if not Path("data/train").exists():
        print("📦 학습 데이터가 없습니다. 이미지 분할을 시작합니다...")
        subprocess.run(["python", "split_food101.py"], check=True)

def train_model_if_needed():
    if not Path("food_model.h5").exists():
        print("🧠 모델이 없습니다. 학습을 시작합니다...")
        subprocess.run(["python", "Foodimage_AI.py"], check=True)

def predict_food(img_path):
    print("🔍 이미지를 분석하여 음식을 예측합니다...")

    model = tf.keras.models.load_model('food_model.h5')

    # 분류 클래스 예시 (추후 자동화 가능)
    class_labels = ['apple_pie', 'bibimbap', 'pizza', 'ramen']  # 실제 train_data.class_indices와 일치시켜야 함

    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    pred_index = np.argmax(pred)
    pred_class = class_labels[pred_index]

    print(f"✅ 예측 결과: {pred_class}")
    return pred_class

def main():
    # 1. 데이터 확인 및 분할
    split_data_if_needed()

    # 2. 모델 확인 및 학습
    train_model_if_needed()

    # 3. 테스트 이미지 예측
    test_img = "test_images/test.jpg"
    if not Path(test_img).exists():
        print(f"⚠️ 테스트 이미지 '{test_img}' 가 존재하지 않습니다.")
        return

    food_name = predict_food(test_img)

    # 4. 영양 정보 출력
    get_nutrition_info(food_name)

if __name__ == "__main__":
    main()