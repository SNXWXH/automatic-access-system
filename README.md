# 파이 카메라를 통한 자동 출입 시스템

### OpenCV
1. git clone 을 사용해 프로젝트 다운  
[OpenCV](https://github.com/opencv/opencv)

2. OpenCV 설치

```
python -m pip install opencv-python
python -m pip install opencv-contrib-python
python -m pip install opencv-python-headless
python -m pip install opencv-contrib-python-headless
```

### Finger
1. Adafruit Fingerprint Sensor 라이브러리 다운

### RFID
1. MFRC522 라이브러리 다운

### face_recognition
1. github에서 face_recognition 프로젝트 파일 내려받기   
https://github.com/ageitgey/face_recognition
   
2. 라즈베리파이 서버에서 cmake, face_recognition 라이브러리 설치   
pip install cmake (cmake 모듈 설치)   
pip install face_recognition (face_recognition 모듈 설치)   
해당 과정에서 numpy와 dlib 모듈이 설치됨   
   
머신러닝 및 영상처리 관련 라이브러리 설치   
pip install --upgrade scikit-learn   
pip install OpenCV-Python   

   
3. 관리자 얼굴 촬영   
admin1_capture.py   
admin2_capture.py   
   
4. 얼굴 인식 API 가져오기   
face_api.py   

### Face Recogiontion
1. 사진 데이터 모으기
2. 학습
3. 인식

### Serial Communication between Python and Arduino
* pySerial 사용
```
pip install pyserial
```


### Submoter
* 서보모터 SG-90 떨림 문제 해결 위해 pigpio 라이브러리 설치
[pigpio](http://abyz.me.uk/rpi/pigpio/index.html)


