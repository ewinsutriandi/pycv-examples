import cv2,mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture("./res/hand-z.mp4")

# inisialisasi mediapipe Hands solution API
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue
    
    image.flags.writeable = False # untuk performa
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # konversi warna ke RGB
    results = hands.process(image) # kirim gambar untuk diproses
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # konversi balik warna ke BGR

    if results.multi_hand_landmarks: # Jika titik penanda tangan (hand landmark) terdeteksi pada gambar
      # gambar seluruh titik, beserta garis penghubungnya      
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(1) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()