'''
Menggunaakan live feed dari kamera
'''
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Gagal mengakses kamera")
    exit()
while True:
    # Mengambil gambar frame-by-frame
    ret, frame = cap.read()    
    # Tampilkan frame
    cv2.imshow('frame', frame)
    # keluar jika user memencet q
    if cv2.waitKey(1) == ord('q'): 
        break
# hentikan proses capture
cap.release()
cv2.destroyAllWindows()