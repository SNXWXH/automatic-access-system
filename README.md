# 파이 카메라를 통한 자동 출입 시스템

## **최종버전 : fianlVersionCode**

## 프로젝트 소개
* Open CV를 이용한 딥러닝 모델 개발을 활용해 관리자 접근 허용
* 아두이노 우노와 라즈베리 파이 간의 시리얼 통신
* 아두이노 우노와 연결된 지문인식센서를 통해 관리자 접근 허용
* 아두이노 우노와 연결된 RFID 센서를 통해 관리자를 제외한 일반 사용자의 접근 허용
* 접근이 허용될 경우 LED 점등 및 LCD 문구 출력, 서보모터를 통해 출입문 열림
* 관리자와 일반 사용자의 접근 경로를 달리해 보안 강화

### 개발 환경
* Arduion IDE
* Python 3.7.9
* Raspberry pi 4

### 프로젝트 기간
* 2022.04.27~2022.06.21

## 사용 기술
### picamera
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-picamera
```

### OpenCV
1. git clone 을 사용해 프로젝트 다운  
* [OpenCV github link](https://github.com/opencv/opencv)
```
git clone https://github.com/opencv/opencv.git
```

2. OpenCV 설치

```
python -m pip install opencv-python
python -m pip install opencv-contrib-python
python -m pip install opencv-python-headless
python -m pip install opencv-contrib-python-headless
```

### Face Recogiontion
1. 사진 데이터 모으기
* face_dataset.py 
* 원하는 경로 파일에 사진 찍어 저장

2. 학습
* face_training.py
```
pip install pillow
```
* 해당 경로 사진 학습 후 모델 yml 파일로 저장

3. 인식
* face_recognition_module.py
* yml 파일 불러와 얼굴 인식

### Finger
* Adafruit Fingerprint Sensor 라이브러리 다운

### RFID
* MFRC522 라이브러리 다운


### Serial Communication between Python and Arduino
* pySerial 사용
```
pip install pyserial
```

### Submoter
* 서보모터 SG-90 떨림 문제 해결 위해 pigpio 라이브러리 설치
* [pigpio 라이브러리](http://abyz.me.uk/rpi/pigpio/index.html)
```
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```

## 완성 모습
![KakaoTalk_20220620_212119486_03](https://user-images.githubusercontent.com/103805632/174601335-a046fee7-cd36-4a2a-b814-fc9de41bcb0e.jpg)
![KakaoTalk_20220620_212133025](https://user-images.githubusercontent.com/103805632/174601346-585e5ead-6e86-4678-824f-e95e0765e6ed.jpg)

### 딥러닝 실행영상
https://user-images.githubusercontent.com/103805632/174602033-7260459b-7644-497a-aecb-684afbb24daa.mp4
### 지문인식 실행영상
https://user-images.githubusercontent.com/103805632/174601879-254beb00-de2c-4303-b55e-4d0ae732e8ef.mp4
### RFID 실행영상
https://user-images.githubusercontent.com/103805632/174601975-009908d2-4e4e-4eda-ab27-4d0cbe6a9c38.mp4
