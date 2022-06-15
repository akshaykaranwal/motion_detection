import cv2
import time
from datetime import datetime
import pandas


first_frame = None
check_status = [None,None]
times = []
df = pandas.DataFrame(columns=['start','end'])

video = cv2.VideoCapture(0)

while True:

    check, frame = video.read()
    status = 0

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame,None,iterations = 2)
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:

        if cv2.contourArea(contour) < 1000:
            continue

        status = 1
        (x,y,w,z) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+z),(0,255,0),3)

    check_status.append(status)

    check_status = check_status[-2:]

    if check_status[-1]==1 and check_status[-2]==0:
        times.append(datetime.now())
    if check_status[-1]==0 and check_status[-2]==1:
        times.append(datetime.now())

    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("threshold frame",thresh_frame)
    cv2.imshow("color frame",frame)

    key = cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(check_status)
print(times)
print(gray)
print(delta_frame)
print(thresh_frame)
print(frame)

for i in range(0,len(times),2):
    df = df.append({'start':times[i],'end':times[i+1]}, ignore_index = True)
df.to_csv("times.csv")
video.release()
cv2.destroyAllWindows()
