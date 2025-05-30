import requests

def get_nutrition_info(food_name):
    # Spoonacular API endpoint
    url = "https://api.spoonacular.com/recipes/guessNutrition"
    
    # 자신의 API 키 입력
    api_key = "d96e951b7fea415695fe7460ee733610"

    # 요청 파라미터 구성
    params = {
        "title": food_name,
        "apiKey": api_key
    }

    # 요청 전송
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"음식: {food_name}")
        print("예상 영양정보:")
        print(f"- 칼로리: {data['calories']['value']} {data['calories']['unit']}")
        print(f"- 탄수화물: {data['carbs']['value']} {data['carbs']['unit']}")
        print(f"- 지방: {data['fat']['value']} {data['fat']['unit']}")
        print(f"- 단백질: {data['protein']['value']} {data['protein']['unit']}")
    else:
        print("API 요청 실패:", response.status_code)

# 테스트용 예시
get_nutrition_info("pizza")
