import cv2 as cv

cap = cv.VideoCapture('./res/head-pose-face-detection-male.mp4')
print(cap.isOpened())
while cap.isOpened():
    ret, frame = cap.read()    
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()