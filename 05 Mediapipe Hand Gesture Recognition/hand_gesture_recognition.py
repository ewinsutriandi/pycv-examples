import math as m

def is_mengepal(hand_landmarks):
    '''
    Mendeteksi apakah telapak tangan sedang mengepal
    '''
    print(len(hand_landmarks[0]))
    if (len(hand_landmarks)==21):
        jempol_pos = hand_landmarks[4]
        tlj_pos = hand_landmarks[8]
        tgh_pos = hand_landmarks[12]
        mns_pos = hand_landmarks[16]
        klk_pos = hand_landmarks[20]
        jarak_ujung_jari = htg_jarak(jempol_pos,tlj_pos) + htg_jarak(tlj_pos,tgh_pos)
        print(jarak_ujung_jari)
    return False


def htg_jarak(t_a,t_b):
    return m.hypot(t_b.y-t_a.y,t_b.x-t_b.x)
