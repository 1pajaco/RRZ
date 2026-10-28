from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt

# a.) Drevo
# f = 10cm ~ 1dm, Z = 14m ~ 140dm, Y = 5m ~ 50dm
# y = -f * Y / Z = -1dm * 50dm / 140dm = 0,3571dm = 35,71mm
#

f = 1
Z = 140
Y = 50
# decimeter
y = f * Y / Z
print(f'a.) Drevo resitev: {y * 100:.2f}mm')

# b.)
f = 100.0
W = 2500.0
Z = 10000.0
a = 0.5

t = np.arange(0, 30.1, 0.1)
vals = a * 1/2 * t**2
vals = f * W / (Z + vals*1000)

plt.plot(t, vals, '.')
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Sirina projekcije')
plt.xticks(np.arange(0, 31, 1)) 
plt.yticks(np.arange(0, 31, 1)) 
plt.suptitle("b")
plt.waitforbuttonpress()
plt.close()

# c.)
# kamera z luknjico se uporablja, ker je preprost model za
# racunati in skicirati, ni popacenja in je poceni
# Medtem ko je leca bolj zahtevan model, saj mora leca upogibati
# svetlobo proti tipalom, kar je pa tezje za predstavo
# Slabosti kamere z luknjico je, da imamo omjeno kolicino svetlobe
# kar pomeni, da potrebujemo zelo dolg exposure time 
# in ce slikamo karkoli v gibanju bo slika meglena
# Leca lahko zbira vec svetlobe zato krajsi exposure time,
# slika je posledicno ostra, svetla in lahko slikamo predmete
# v gibanju, menjava lece nam spreminja goriscno razdaljo,
# slabosti so, da zaradi upogibanja pride do popacenja, drazje,
# bolj zahteven model kamere za predstavo

# d.) 1 inch = 2.54cm = 25.4mm
f = 60 #mm
Z = 95000 #mm
D = 2500 
hpx = 200 # px
# h = ?

p = 25.4 / D
# hpx = h / p ~ najdemo velikost v mm
h = hpx * p
# h = -f * H / Z
# h * Z / -f = H

H = h * Z / f
print(f'd.) Velikost valja je {H:.2f}mm')

# e.)

# folder = Path(__file__).parent / 'src' / 'bottle'
# files = sorted(folder.glob('*.jpg'))
# for f in files:
#     im = cv2.imread(f)

#     plt.clf()
#     plt.imshow(im)
#     plt.title(f.name) 
#     plt.pause(0.1) 
#     obj = plt.ginput(2, timeout=0)

#     (x1, y1), (x2, y2) = obj
#     h = np.abs(y2 - y1)
#     harr.append(h)

# hfarr = np.array([np.float64(414.91935483870964), np.float64(376.2096774193549), np.float64(289.11290322580646), np.float64(408.8709677419354), np.float64(223.79032258064524), np.float64(354.4354838709677)])
hbarr = np.array([np.float64(420.9677419354837), np.float64(377.4193548387095), np.float64(353.2258064516128), np.float64(318.14516129032256), np.float64(283.0645161290322), np.float64(206.85483870967744)])
Zb = np.array([65.6, 73, 79.2, 86.7, 96.5, 131.7])
Zf = np.array([68, 76.5, 99.5, 70, 124.3, 80])
H = 24

# h = -f * (H / Z)
# f = h * Z / H

farr = hbarr * (Zb / H)
f = np.mean(farr[:5])
print(f'e.) f: {f:.1f} std: {np.std(farr[:5]):.1f}')

hexp = f * (H / Zb[5])

print(f'Pričakovana velikost: {hexp}, "dejanska" velikost: {hbarr[5]}, napaka: {hexp - hbarr[5]}')












