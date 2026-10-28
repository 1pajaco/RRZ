from matplotlib import pyplot as plt
import matplotlib.colors as cl
import numpy as np
import cv2 as cv

# a.)
RGB = np.asarray([255, 34, 126])

RGBn = (RGB / 255).astype(np.float32)
print(f'a.) Target value: {cl.rgb_to_hsv(RGBn)}')

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

print(f'What i got: {Hhsv}, {Shsv}, {Vhsv}\n')

# b.)
HSV = np.asarray([0.65, 0.7, 0.15])
print(f'b.) Target value: {cl.hsv_to_rgb(HSV) * 255}')

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

print(f'What i got: {R}, {G}, {B}\n')

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
plt.suptitle('c')

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

# d
_, BinImB = cv.threshold(imB, 150, 255, cv.THRESH_BINARY)
plt.subplot(1, 2, 1)
plt.imshow(imT)
plt.subplot(1, 2, 2)
plt.imshow(BinImB, cmap='gray')
plt.suptitle('d')
plt.waitforbuttonpress()
plt.close()

# e.)
# timB = imB.astype(np.float32)
# timT = imT.astype(np.float32)
# imBn = timB / np.sum(timT, axis=2)

# _, BinImB = cv.threshold(imBn, 0.5, 1.0, cv.THRESH_BINARY)

# plt.subplot(1, 2 , 1)
# plt.imshow(imT)
# plt.subplot(1, 2 , 2)
# plt.imshow(BinImB, cmap='gray')
# plt.suptitle('e')
# plt.waitforbuttonpress()
# plt.close()

from matplotlib.widgets import Slider

imBn = imB / np.maximum(imT.astype(np.float32).sum(axis=2), 1)

fig, (ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(bottom=0.2)
fig.suptitle('e')
ax1.imshow(imT)
shown = ax2.imshow(imBn > 0.5, cmap='gray', vmin=0, vmax=1)

slider = Slider(plt.axes([0.25, 0.05, 0.5, 0.04]), 'Prag', 0, 1, valinit=0.5, valstep=0.01)
slider.on_changed(lambda v: (shown.set_data(imBn > v), fig.canvas.draw_idle()))
plt.show()

# f

min = 124 / 255
max = 150 / 255

timT = (imH > min) & (imH < max)

plt.subplot(2, 2, 1)
plt.imshow(imT)
plt.suptitle('f')

plt.subplot(2, 2, 2)
plt.imshow(timT, cmap='gray')

plt.subplot(2, 2, (3, 4))
plt.imshow(np.meshgrid(np.linspace(0, 1, 255), np.ones((10, 1)))[0],
cmap=plt.cm.hsv)
plt.suptitle('f')

plt.waitforbuttonpress()
plt.close()


# g.)
from pathlib import Path
im = cv.imread('./src/apples.jpg')
im = im[:, :, ::-1]

im_hsv = cl.rgb_to_hsv((im / 255).astype(np.float32))
H = im_hsv[..., 0]

m_h = (H > 0.16) & (H < 0.25)
m_hsv = (m_h) & (im_hsv[..., 1] > 0.15)

plt.subplot(2, 2, (1, 2))
plt.imshow(im)
plt.title('Original')

plt.subplot(2, 2, 3)
plt.title('Samo hue')
plt.imshow(m_h, cmap='gray')

plt.subplot(2, 2, 4)
plt.title('se S')
plt.imshow(m_hsv, cmap='gray')
plt.suptitle('g part1')

plt.waitforbuttonpress()
plt.close()

# 0.026570046
# 0.9782609
# 0.033549782
# 0.97530866
# 0.99856323
# 0.011538462
# 0.011538462

m_h = (H > 0.95) | (H < 0.03) 
m_hsv = m_h & (im_hsv[..., 1] > 0.25)

plt.subplot(2, 2, (1, 2))
plt.imshow(im)
plt.title('Original')

plt.subplot(2, 2, 3)
plt.title('Samo hue')
plt.imshow(m_h, cmap='gray')

plt.subplot(2, 2, 4)
plt.title('Se S')
plt.imshow(m_hsv, cmap='gray')
plt.suptitle('g_part2')

plt.waitforbuttonpress()
plt.close()

# 0.38020834
# 0.38505745
# 0.29166666
# 0.36507937
# 0.34397164
# 0.27777776
# 0.23333333
# 0.36666667

# plt.imshow(H, cmap='hsv', vmin=0, vmax=1)
# pts = plt.ginput(8)
# plt.close()
# for x, y in pts:
#     print(H[int(y), int(x)])

folder = Path(__file__).parent / 'src' / 'bottle'
files = sorted(folder.glob('*.jpg'))

i = 1

for file in files:    
    im = cv.imread(file)
    im = im[..., ::-1]
    im_hsv = cl.rgb_to_hsv((im / 255).astype(np.float32))

    H = im_hsv[..., 0]
        
    m_h = (H < 0.38) & (H > 0.27)
    m_hsv = (m_h) & (im_hsv[..., 1] > 0.25)

    plt.subplot(6, 2, i)
    plt.imshow(im)

    plt.subplot(6, 2, i+1)
    plt.imshow(m_hsv, cmap='gray')
    plt.suptitle('g_part3')

    i += 2

plt.show()

# h.)
def im_mask(im, bim):

    # im = np.where(bim[..., None], im, 0)
    return  im * bim[..., None]

im = cv.imread('./src/apples_640x360.jpg')
im = im[..., ::-1]

mask = cv.imread('./src/umbrellas.jpg', cv.IMREAD_GRAYSCALE)
mask = mask < 50
plt.subplot(1, 2, 1)
plt.imshow(im_mask(im, mask))

plt.subplot(1, 2, 2)
plt.imshow(mask, cmap='gray')
plt.suptitle('h')
plt.show()
