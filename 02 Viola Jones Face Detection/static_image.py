import cv2

# Load algoritma viola jones untuk deteksi wajah
face_cascade = cv2.CascadeClassifier('./res/haarcascade_frontalface_default.xml')

img = cv2.imread('./res/the-beatles.jpg',cv2.IMREAD_COLOR)
while True:        
    # konversi frame ke grayscale
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        
    # deteksi wajah menggunakan algoritma viola jones
    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)
    # gambar kotak di area wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)    
    cv2.imshow('frame', img)        
    if cv2.waitKey(0):
        break
cv2.destroyAllWindows()
        
