from matplotlib import pyplot as plt
import matplotlib.colors as cl
import numpy as np
import cv2 as cv

# a.)
RGB = np.asarray([255, 34, 126])

RGBn = (RGB / 255).astype(np.float32)
print(f'Target value: {cl.rgb_to_hsv(RGBn)}')

Chigh = np.max(RGBn)
Clow = np.min(RGBn)
delta = Chigh - Clow

Rt = (Chigh - RGBn[0]) / delta
Gt = (Chigh - RGBn[1]) / delta
Bt = (Chigh - RGBn[2]) / delta

# H calc
Ht = 0.0
if delta == 0:
    pass
elif Chigh == RGBn[0]:
    Ht = Bt - Gt
elif Chigh == RGBn[1]:
    Ht = Rt - Bt + 2
elif Chigh == RGBn[2]:
    Ht = Gt - Rt + 4

Hhsv = 0.0
if Ht < 0:
    Hhsv = 1/6 * (Ht + 6)
else:
    Hhsv = 1/6 * Ht

# S calc
Shsv = 0.0

if Chigh > 0:
    Shsv = delta / Chigh
else:
    Shsv = 0

# V calc
Vhsv = Chigh / 1.0

print(f'What i got: {Hhsv}, {Shsv}, {Vhsv}')

# b.)
HSV = np.asarray([0.65, 0.7, 0.15])
print(f'Target value: {cl.hsv_to_rgb(HSV) * 255}')

Ht = (6 * HSV[0]) % 6
c1 = np.floor(Ht)
c2 = Ht - c1

x = (1.0 - HSV[1]) * HSV[2]
y = (1.0 - (HSV[1] * c2)) * HSV[2]
z = (1.0 - (HSV[1] * (1.0 - c2))) * HSV[2]
v = HSV[2]

RGBt = np.zeros(3, dtype=np.float32)

match c1:
    case 0:
        RGBt = [v, z, x]
    case 1:
        RGBt = [y, v, x]
    case 2:
        RGBt = [x, v, z]
    case 3:
        RGBt = [x, y, v]
    case 4:
        RGBt = [z, x, v]
    case 5:
        RGBt = [v, x, y]

R = np.minimum(np.round(256.0 * RGBt[0]), 255.0)
G = np.minimum(np.round(256.0 * RGBt[1]), 255.0)
B = np.minimum(np.round(256.0 * RGBt[2]), 255.0)

print(f'What i got: {R}, {G}, {B}')

# c)
imT = cv.imread('./src/trucks.jpg')
# im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
imT = imT[..., ::-1]

imR = imT[..., 0]
imG = imT[..., 1]
imB = imT[..., 2]

plt.subplot(2, 4, 1)
plt.imshow(imT)
plt.title('RGB')

plt.subplot(2, 4, 2)
plt.imshow(imR, cmap='gray')
plt.title('Rdeca')

plt.subplot(2, 4, 3)
plt.imshow(imG, cmap='gray')
plt.title('Zelena')

plt.subplot(2, 4, 4)
plt.imshow(imB, cmap='gray')
plt.title('Modra')

im = imT.astype(np.float32)
im = im / 255
im = cv.cvtColor(im, cv.COLOR_RGB2HSV)
im[..., 0] = im[..., 0] / 360

# Reprenzentacija barve 
imH = im[..., 0]
# Koliko je barva "umazna" 0.0 cista, 1.0 zelo meglena/veliko sive
imS = im[..., 1]
# Koliko je barva svetna 0.0 zelo temna 1.0 zelo svetla
imV = im[..., 2]

plt.subplot(2, 4, 6)
plt.imshow(imH, cmap='hsv', vmin=0.0, vmax=1.0)
plt.title('Hue')

plt.subplot(2, 4, 7)
plt.imshow(imS, cmap='gray', vmin=0.0, vmax=1.0)
plt.title('Saturation')

plt.subplot(2, 4, 8)
plt.imshow(imV, cmap='gray', vmin=0.0, vmax=1.0)
plt.title('Value')

plt.waitforbuttonpress()
plt.close()

# d * 
_, BinImB = cv.threshold(imB, 150, 255, cv.THRESH_BINARY)
plt.subplot(1, 2, 1)
plt.imshow(imT)
plt.subplot(1, 2, 2)
plt.imshow(BinImB, cmap='gray')
plt.waitforbuttonpress()
plt.close()

# e.)
timB = imB.astype(np.float32)
timT = imT.astype(np.float32)
imBn = timB / np.sum(timT, axis=2)

_, BinImB = cv.threshold(imBn, 0.5, 1.0, cv.THRESH_BINARY)

plt.subplot(1, 2 , 1)
plt.imshow(imT)
plt.subplot(1, 2 , 2)
plt.imshow(BinImB, cmap='gray')
plt.waitforbuttonpress()
plt.close()


plt.figure()
plt.imshow(np.meshgrid(np.linspace(0, 1, 255), np.ones((10, 1)))[0],
cmap=plt.cm.hsv)
plt.show()
