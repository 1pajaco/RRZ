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
print(f'Drevo resitev: {y * 100:.2f}mm')

# b.)
f = 100.0
W = 2500.0
Z = 10000.0
a = 0.5

t = np.arange(0, 30.1, 0.1)
vals = a * 1/2 * t**2
vals = f * W / (Z + vals*1000)
# print(vals)
# print(vals.ndim)
# print(vals.shape)

plt.plot(t, vals, '.')
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Sirina projekcije')
plt.xticks(np.arange(0, 31, 1)) 
plt.yticks(np.arange(0, 31, 1)) 
plt.show()

# c.)
# kamera z luknjico se uprablja, ker je preprost model za
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
D = 2500 #mm
hpx = 200 # px
# h = ?

p = 25.4 / 2500
# hpx = h / p ~ najdemo velikost v mm
h = hpx * p
# h = -f * H / Z
# h * Z / -f = H

H = h * Z / f
print(f'Velikost vlaja je {H:4f}mm')

# e.)




