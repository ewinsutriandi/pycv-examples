import cv2
import mediapipe as mp
import hand_gesture_recognition as hgc

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# inisialisasi mediapipe Hands dari hands solution API
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# load gambar tangan
img = cv2.imread('./res/fist_square.jpg',cv2.IMREAD_COLOR)
#img = cv2.flip(img,1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # konversi warna ke RGB
image_height, image_width, c = img.shape # get image shape

# proses gambar
results = hands.process(img)
if results.multi_hand_landmarks:
    for landmarks in results.multi_hand_landmarks:        
        # deteksi tangan membuka
        terbuka = hgc.is_membuka(landmarks.landmark)
        # tulis keterangan
        pos_text = (int(landmarks.landmark[0].x * image_width),int(landmarks.landmark[0].y * image_height))
        print(pos_text)
        if terbuka:            
            cv2.putText(img,"MEMBUKA",pos_text,cv2.FONT_HERSHEY_SIMPLEX,1,(0,100,100),1,cv2.LINE_AA)

img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR) # konversi balik ke BGR
cv2.imshow('Annotated image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()