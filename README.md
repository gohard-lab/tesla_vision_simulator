# 2021년 당시 Tesla Vision Edge Case Simulator

📺 상세 분석 및 시연 영상
이 시뮬레이터가 실제로 그림자나 역광을 어떻게 장애물로 오인하는지, 그리고 테슬라의 레이더 제거 결정에 대한 개발자 관점의 상세한 분석은 아래 유튜브 영상에서 확인하실 수 있습니다.

YouTube 영상 (잡학다식 개발자): https://www.youtube.com/watch?v=xWrnxjh1GnY


파이썬(Python)과 OpenCV를 활용하여 테슬라의 '비전 온리(Vision Only)' 자율주행 시스템이 현실 도로에서 직면하는 엣지 케이스(팬텀 브레이킹 등)를 시각적으로 분석하는 기초 시뮬레이터입니다.

## 🚨 핵심 주제: 이론과 현실의 간극

* **교과서적 이론:** 고도화된 AI 비전 모델(Occupancy Networks 등)은 방대한 데이터 학습을 통해 2D 카메라 이미지 속 객체를 3D 공간으로 완벽하게 재구성하고 거리를 판단할 수 있습니다.
* **실제 도로의 현실:** 그러나 실제 도로는 통제된 환경이 아닙니다. 강한 역광, 터널 입구의 급격한 조도 변화, 바닥에 짙게 깔린 그림자 등 예측 불가능한 '엣지 케이스'가 난무합니다. 과거에는 레이더가 전파를 쏴서 "물리적인 장애물이 없다"라고 크로스체크를 수행했지만, 레이더가 배제된 순수 비전 모델은 단순한 빛과 명암의 왜곡을 '거대한 장벽'으로 오탐지(False Positive)할 위험을 내포합니다. 이것이 센서 퓨전(Sensor Fusion) 부재로 인한 팬텀 브레이킹의 핵심 원리입니다.

이 프로젝트는 블랙박스 영상을 통해 컴퓨터 비전 알고리즘이 빛의 장난에 어떻게 속는지, 그 구조적 취약점을 직관적으로 확인하기 위해 작성되었습니다.

## ⚙️ 기술 스택 및 환경
* **Language:** Python 3.9+
* **Library:** OpenCV (`opencv-python`)
* **Dependency Management:** `pyproject.toml`

## 🚀 설치 및 실행 방법

본 프로젝트는 레거시 방식인 `requirements.txt` 대신, 모던 파이썬 패키징 표준인 `pyproject.toml`을 사용하여 의존성을 관리합니다.

1. 저장소를 클론(Clone)합니다.
```bash
git clone [https://github.com/gohard-lab/tesla_vision_simulator.git](https://github.com/gohard-lab/tesla_vision_simulator.git)
cd tesla_vision_simulator