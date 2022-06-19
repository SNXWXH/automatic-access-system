# 파이 카메라를 통한 자동 출입 시스템
## 프로젝트 소개
* Open CV를 이용한 딥러닝 모델 개발을 활용해 관리자 접근 허용
* 아두이노 우노와 라즈베리 파이 간의 시리얼 통신
* 아두이노 우노와 연결된 지문인식센서를 통해 관리자 접근 허용
* 아두이노 우노와 연결된 RFID 센서를 통해 관리자를 제외한 일반 사용자의 접근 허용
* 접근이 허용될 경우 LED 점등 및 LCD 문구 출력, 서보모터를 통해 출입문 열림
* 관리자와 일반 사용자의 접근 경로를 달리해 보안 강화
<br/><br/>
### 개발 환경
* Arduion IDE
* Python 3.7.9
* Raspberry pi 4
<br/><br/>
## 사용 기술
### picamera
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-picamera
```
<br/><br/>
### OpenCV
1. git clone 을 사용해 프로젝트 다운  
* [OpenCV github link](https://github.com/opencv/opencv)
```
git clone https://github.com/opencv/opencv.git
```
<br/>
2. OpenCV 설치

```
python -m pip install opencv-python
python -m pip install opencv-contrib-python
python -m pip install opencv-python-headless
python -m pip install opencv-contrib-python-headless
```
<br/><br/>
### Face Recogiontion
1. 사진 데이터 모으기
* face_dataset.py 
* 원하는 경로 파일에 사진 찍어 저장
* <br/>
2. 학습
* face_training.py
```
pip install pillow
```
* 해당 경로 사진 학습 후 모델 yml 파일로 저장
<br/>
3. 인식
* face_recognition_module.py
* yml 파일 불러와 얼굴 인식
<br/><br/>
### Finger
1. Adafruit Fingerprint Sensor 라이브러리 다운
<br/><br/>
### RFID
1. MFRC522 라이브러리 다운
<br/><br/>
### face_recognition
1. github에서 face_recognition 프로젝트 파일 내려받기   
https://github.com/ageitgey/face_recognition
<br/>   
2. 라즈베리파이 서버에서 cmake, face_recognition 라이브러리 설치   
pip install cmake (cmake 모듈 설치)   
pip install face_recognition (face_recognition 모듈 설치)   
해당 과정에서 numpy와 dlib 모듈이 설치됨   
   
머신러닝 및 영상처리 관련 라이브러리 설치   
pip install --upgrade scikit-learn   
pip install OpenCV-Python   

<br/>   
3. 관리자 얼굴 촬영   
admin1_capture.py   
admin2_capture.py   
<br/>   
4. 얼굴 인식 API 가져오기   
face_api.py   

<br/><br/>
### Serial Communication between Python and Arduino
* pySerial 사용
```
pip install pyserial
```
<br/><br/>
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
<br/><br/>
## 완성 모습

