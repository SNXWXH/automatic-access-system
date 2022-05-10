import cv2
import socket
import numpy as np
import time

TCP_IP = '192.168.124.1' # Server에서 확인한 IP주소 입력
TCP_PORT = 135 # port번호는 개인에 따라 다시 설정할 것

startTime = time.time()  # 현재 시간 저장
## TCP 사용
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## server ip, port
sock.connect(('192.168.124.1', 135))

## webcam 이미지 capture
capture = cv2.VideoCapture(0)
## 0~100에서 90의 이미지 품질로 설정 (default = 95)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    # 비디오의 한 프레임씩 읽는다.
    # 제대로 읽으면 ret = True, 실패면 ret = False, frame에는 읽은 프레임
    ret, frame = capture.read()
    # cv2. imencode(ext, img [, params])
    # encode_param의 형식으로 frame을 jpg로 이미지를 인코딩한다.
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    # frame을 String 형태로 변환
    data = np.array(frame)
    stringData = data.tobytes()

    # 서버에 데이터 전송
    sock.sendall((str(len(stringData))).encode().ljust(16) + stringData)

    if time.time() - startTime > 30: # 30초 이후에 영상전송 종료
        break

capture.release()