#face_api.py

import face_recognition
import cv2
import numpy as np

# 기본 카메라(webcam #0)에 대한 참조를 가져옴
video_capture = cv2.VideoCapture(0)

# 관리자1 사진을 로드하고 이를 인식하기
admin1_image = face_recognition.load_image_file("admin1_0.jpg")
admin1_image = face_recognition.load_image_file("admin1_1.jpg")
admin1_image = face_recognition.load_image_file("admin1_2.jpg")
admin1_image = face_recognition.load_image_file("admin1_3.jpg")
admin1_image = face_recognition.load_image_file("admin1_4.jpg")
admin1_face_encoding = face_recognition.face_encodings(admin1_image)[0]

# 관리자2 사진을 로드하고 이를 인식하기
admin2_image = face_recognition.load_image_file("admin2_0.jpg")
admin2_image = face_recognition.load_image_file("admin2_1.jpg")
admin2_image = face_recognition.load_image_file("admin2_2.jpg")
admin2_image = face_recognition.load_image_file("admin2_3.jpg")
admin2_image = face_recognition.load_image_file("admin2_4.jpg")
admin2_face_encoding = face_recognition.face_encodings(admin2_image)[0]

# 알려진 얼굴 인코딩 및 해당 이름의 배열 생성
known_face_encodings = [
    admin1_face_encoding,
    admin2_face_encoding
]
known_face_names = [
    "admin1",
    "admin2"
]

# 일부 변수 초기화
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 단일 비디오 프레임 잡기
    ret, frame = video_capture.read()

    # 비디오 프레임 크기를 1/4로 조정하여 얼굴 인식 처리 속도 향상
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # 이미지를 BGR 색상 (OpenCV가 사용하는 색)에서 RGB 색상 (face_recognition이 사용하는 색)으로 변환
    rgb_small_frame = small_frame[:, :, ::-1]

    # 다른 모든 비디오 프레임만 처리하여 시간 절약
    if process_this_frame:
        # 비디오의 현재 프레임에서 모든 얼굴 인코딩 찾기
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # 얼굴이 알려진 얼굴과 일치하는지 확인
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # known_face_encodings에서 일치하는 항목이 있으면, 첫 번째 항목 사용
            # 일치하는 경우:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # 또는 새 얼굴까지의 거리가 가장 작은 알려진 얼굴 사용
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # 결과 표시
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # 감지한 프레임이 1/4 크기로 확장되었으므로 얼굴 위치 확장
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # 얼굴 주위에 상자 생성
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 얼굴 아래에 이름이 있는 레이블 그리기
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 결과 영상 표시
    cv2.imshow('Video', frame)

    # 종료시 키보드의 'q'를 누르기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠에 핸들을 놓음
video_capture.release()
cv2.destroyAllWindows()