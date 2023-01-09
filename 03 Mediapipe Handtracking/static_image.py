import cv2
import mediapipe as mp

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
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # konversi warna ke RGB

# proses gambar
results = hands.process(img)

image_height, image_width, _ = img.shape
annotated_image = img.copy() # salin gambar untuk ditandai
# beri tanda pada titik penanda tangan
for hand_landmarks in results.multi_hand_landmarks:
    mp_drawing.draw_landmarks(
        annotated_image,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_drawing_styles.get_default_hand_landmarks_style(),
        mp_drawing_styles.get_default_hand_connections_style())
annotated_image = cv2.cvtColor(annotated_image,cv2.COLOR_RGB2BGR) # konversi balik ke BGR
cv2.imshow('Annotated image',annotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()