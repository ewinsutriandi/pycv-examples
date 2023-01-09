import cv2 as cv

cap = cv.VideoCapture('./res/head-pose-face-detection-male.mp4')

while cap.isOpened():
    ret, frame = cap.read()    
    cv.imshow('frame', frame)
    if cv.waitKey(50) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()