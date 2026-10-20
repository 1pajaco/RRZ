import numpy as np
# a.) 3 bitna slikovna slika 2^3
im = np.asarray(
[[5, 3, 2, 7, 1],
 [7, 1, 0, 0, 0],
 [4, 5, 7, 1, 1],
 [1, 3, 2, 1, 1],
 [5, 3, 1, 6, 3]]
)

tim = np.reshape(im, -1)

# hist = np.bincount(tim) 
# hist, _ = np.histogram(im, bins=2, range=(0, 8))
hist = (tim[:, None] == np.arange(8)).sum(axis=0)
print(f'Histogram: {hist}')

# b.)
# kum_hist = np.cumsum(hist))
# kum_hist = (hist * (np.arange(8)[:, None] >= np.arange(8))).sum(axis=1)
kum_hist = np.tri(8, dtype=int) @ hist
print(f'Kumulativni histogram: {kum_hist}')

# c.) odvisno koliko kosev bi imeli, glede na bite bi nas
# histogram lahko zavzemal vrednosti med 0 in 15 (2^4 = 16)
# kar pomeni da imamo lahko 16 binnov, 7, 3 ali celo 1
# zelo odvisno kaj zelimo da nas histogram prikazuje

