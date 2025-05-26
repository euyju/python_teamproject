# 음식 인식 AI – 파이썬 프로그래밍 팀프로젝트

> 본 프로젝트는 Python과 딥러닝을 활용하여 음식 이미지를 분류하고,  
> 예측된 음식의 영양 정보를 검색/출력하는 파이썬 프로그래밍 팀프로젝트입니다.

---

# 프로젝트 개요

- 음식 사진을 입력하면  
- AI가 음식 종류를 예측하고  
- 해당 음식의 영양정보(API)까지 출력해주는 시스템입니다.

---

## 사용 기술

| 분야 | 기술 |
|------|------|
| 언어 | Python 3.x |
| 딥러닝 | TensorFlow (CNN 모델) |
| 데이터 | Food-101 (Kaggle 공개 데이터셋) |
| 웹 데이터 | Open Food Facts API 또는 자체 DB |
| 개발환경 | VS Code, GitHub |

---

## 폴더 구조

```plaintext
FoodProject/
├── data/
│   ├── train/         # 학습 이미지 (음식별 폴더로 분류됨)
│   └── val/           # 검증 이미지
├── images/            # 원본 Food-101 전체 이미지
├── test_images/       # 테스트용 음식 사진
├── food_model.h5      # 학습된 모델
├── Foodimage_AI.py    # AI 학습 코드
├── predict.py         # 예측 및 결과 출력 코드
├── split_food101.py   # 이미지 분할 스크립트
└── README.md          # 📄 이 문서
