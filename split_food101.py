import os
import shutil
import random
from pathlib import Path

# 실제 Food-101 이미지 경로
src_dir = Path(r"G:/내 드라이브/2025 1학기/과제/파이썬프로그래밍/FoodProject/python_teamproject/food-101/food-101/images")
train_dir = Path("data/train")
val_dir = Path("data/val")

# 카테고리 폴더 탐색
categories = [folder.name for folder in src_dir.iterdir() if folder.is_dir()]

for category in categories:
    image_paths = list((src_dir / category).glob("*.jpg"))
    random.shuffle(image_paths)

    train_cutoff = int(0.8 * len(image_paths))
    train_images = image_paths[:train_cutoff]
    val_images = image_paths[train_cutoff:]

    # 폴더 생성
    (train_dir / category).mkdir(parents=True, exist_ok=True)
    (val_dir / category).mkdir(parents=True, exist_ok=True)

    # 이미지 복사
    for img_path in train_images:
        shutil.copy(img_path, train_dir / category / img_path.name)
    for img_path in val_images:
        shutil.copy(img_path, val_dir / category / img_path.name)

print("✅ 이미지 분할 완료: data/train, data/val 폴더 생성됨")