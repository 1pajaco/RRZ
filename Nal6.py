import cv2 as cv
import numpy as np
import matplotlib.colors as cl

# a
cap = cv.VideoCapture(0) # 0 = privzeta spletna kamera
# Namesto številke lahko podamo tudi ime video datoteke
# Zanka za pridobitev naslednje slike

i = 0
while(True):
    i += 1
    # Poskusimo pridobiti trenutno sliko s spletne kamere
    ret, frame = cap.read()
    # Če to ni mogoče (kamera izključena, itd.), končamo z izvajanjem funkcije
    if not ret:
        break
    # Prikaži trenutno sliko
    cv.imshow(f'frame1', frame)
    cv.imshow(f'frame2', frame)
    # Ob pritisku tipke 'q' prekini izvajanje funkcije
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# Zapri kamero in okno
cap.release()
cv.destroyAllWindows()

#b
cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow(f'Original', frame)
    cv.imshow(f'Sivinska slika', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

#c
cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)
    im = frame[..., ::-1]
    im_hsv = cl.rgb_to_hsv((im / 255).astype(np.float32))

    H = im_hsv[..., 0]
        
    m_h = (H < 0.38) & (H > 0.27)
    m_hsv = (m_h) & (im_hsv[..., 1] > 0.25)

    kernal = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10,10))
    m_hsv = m_hsv.astype(np.uint8) * 255
    m_hsv = cv.morphologyEx(m_hsv, cv.MORPH_CLOSE, kernal)
    m_hsv = cv.morphologyEx(m_hsv, cv.MORPH_OPEN, kernal)

    cnt, _ = cv.findContours(m_hsv, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(frame, cnt, -1, (0, 0, 255), 2)

    cv.imshow('Tracking', m_hsv)
    cv.imshow('Outline', frame)   

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

