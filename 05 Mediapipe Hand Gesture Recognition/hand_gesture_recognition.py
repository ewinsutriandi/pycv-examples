import math as m

def is_membuka(landmark):
    '''
    Mendeteksi apakah telapak tangan sedang membuka
    '''
    
    idxs_ujung = [4,8,12,16,20] # indeks untuk ujung jempol s.d kelingking    
    idxs_pangkal = [2,5,9,13,17] # indeks untuk pangkal jempol s.d kelingking        
    
    # cek apakah seluruh pangkal di bawah seluruh ujung jari bersesuaian
    for i in range(len(idxs_pangkal)):
        idx_ujung = idxs_ujung[i]
        idx_pangkal = idxs_pangkal[i]
        if landmark[idx_ujung].y > landmark[idx_pangkal].y:
            return False        
    
    # cek apakah jari-jari membuka dari jarak ujung dibanding pangkal jari
    jarak_ujung = htg_jarak_multi_point(landmark,idxs_ujung)
    jarak_pangkal = htg_jarak_multi_point(landmark,idxs_pangkal)
    print("{:.2f}".format(jarak_ujung / jarak_pangkal))    
    if jarak_ujung / jarak_pangkal > 1.5:
        return True
    return False

def is_mengepal(landmark):
    '''
    Mendeteksi apakah telapak tangan sedang mengepal
    '''
    # print(processed_hands.multi_handedness)
    idxs_ujung = [4,8,12,16,12] # indeks untuk ujung jempol s.d kelingking
    idxs_pangkal = [2,5,9,13,17] # indeks untuk pangkal jempol s.d kelingking        
    jarak_ujung = htg_jarak_multi_point(landmark,idxs_ujung)
    jarak_pangkal = htg_jarak_multi_point(landmark,idxs_pangkal)
    print("{:.2f}".format(jarak_ujung / jarak_pangkal))
    if jarak_ujung / jarak_pangkal > 2:
        return True
    return False


def htg_jarak(t_a,t_b):
    return m.hypot(t_b.y-t_a.y,t_b.x-t_b.x)

def htg_jarak_multi_point(landmark,idxs):
    jarak = 0
    for i in range(len(idxs)-1):
        idx = idxs[i]
        idx_next = idxs[i+1]
        jarak += htg_jarak(landmark[idx],landmark[idx_next])
    return jarak