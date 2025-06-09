from pathlib import Path
from FoodAPI import get_nutrition_info
from predict import predict_food

def main():
    test_img = "test_images/test.jpg"
    if not Path(test_img).exists():
        print(f" 테스트 이미지 '{test_img}' 가 존재하지 않습니다.")
        return

    food_name = predict_food(test_img)
    get_nutrition_info(food_name)

if __name__ == "__main__":
    main()