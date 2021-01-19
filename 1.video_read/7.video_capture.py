#!/usr/bin/env python3
# 0207.py
import cv2

# 1. video 객체 획들

#카메라이용
#cap = cv2.VideoCapture(0)  # 0번 카메라

#video 영상이용
cap = cv2.VideoCapture('./data/vtest.avi')


#2. frame size 설정

#카메라 이용시 frame size 조절
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


#cap.get  비디오 프레임의 가로 세로 크기 속성을 읽어 정수로 변환 후
           #frame size에 할당
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)


#무한반복루프

while True:   
    # 3. 프레임 획득
    retval, frame = cap.read()
    # 프레임에 값이 없다면 무한반복 종료
    if not retval:
        break

    # 4. 프레임 출력
    cv2.imshow('frame',frame)
    
    # 종료 키 설정
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
# 5. 정상종료
if cap.isOpened(): #비디오 객체가 열려있다면
    cap.release()  #비디오 획득 객체 해제
cv2.destroyAllWindows() # 윈도우 창 종료