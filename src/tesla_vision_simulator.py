import cv2
import os
import sys
from tracker import log_app_usage

video_path = 'dashcam_footage.mp4'
if not os.path.exists(video_path):
    print(f"에러: {video_path} 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
    sys.exit(1)


def detect_vehicles(video_path):
    # 비디오 캡처 객체 초기화
    cap = cv2.VideoCapture(video_path)
    
    # [핵심] 사전에 훈련된 구형 자동차 인식 모델(Haar Cascade) 로드
    # 테슬라 FSD는 Occupancy Networks 기반 딥러닝 모델을 사용
    # 현업에서는 YOLO 등 딥러닝 기반 모델을 주로 사용
    # 이 XML은 단순 명암 패턴만 찾는 '탁상공론' 수준
    car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 연산 속도를 높이기 위해 프레임 크기를 가로 640 픽셀로 대폭 축소
        # frame = cv2.resize(frame, (640, 360))

        # 인식률을 높이기 위해 프레임을 흑백으로 변환
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 자동차 객체 탐지 수행
        cars = car_cascade.detectMultiScale(gray_frame, 1.1, 1)

        # 탐지된 자동차 주위에 사각형 그리기 (시각화)
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)

        # 결과 화면 출력
        cv2.imshow('Tesla Vision Simulator', frame)

        # 'q' 키를 누르면 종료
        # 대기 시간을 33ms에서 1ms로 줄여서, 연산이 끝나는 대로 지연 없이 바로바로 다음 프레임으로 넘어가게
        if cv2.waitKey(1) == ord('q'):
            break

    # 보안 및 리소스 관리를 위해 사용이 끝난 객체 반환
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    log_app_usage("tesla-vision-simulator", "vision_simulator_started")
    detect_vehicles('dashcam_footage.mp4')
