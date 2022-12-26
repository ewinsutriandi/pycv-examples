import cv2

# Load algoritma viola jones untuk deteksi wajah
face_cascade = cv2.CascadeClassifier('./res/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Gagal mengakses kamera")
    exit()
while True:    
    ret, frame = cap.read()
    # konversi frame ke grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        
    # deteksi wajah menggunakan algoritma viola jones
    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4)
    # gambar kotak di area wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)    
    cv2.imshow('frame', frame)    
    if cv2.waitKey(1) == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()