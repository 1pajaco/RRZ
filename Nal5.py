import cv2 as cv
from matplotlib.widgets import Slider
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat

# a 
# original
matrix = np.array([
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1]
])
# first run
m = np.array([
    [ 0,  0, 0, 0, 0,  0, 0, 2, 0],
    [ 0,  0, 0, 3, 0,  0, 0, 2, 2],
    [ 0,  4, 0, 3, 0,  0, 5, 2, 2],
    [ 6,  4, 4, 3, 0,  7, 0, 0, 0],
    [ 6,  0, 0, 3, 3,  0, 0, 0, 0],
    [ 0,  0, 0, 0, 0,  0, 0, 0, 8],
    [ 0,  0, 0, 0, 0,  0, 9, 9, 8],
    [ 0, 10, 0, 0, 0, 11, 9, 9, 8],
    [12, 10, 0, 0, 0,  0, 0, 0, 8]
])
k = {(5, 2), (6, 4), (4, 3), (9, 8), (11, 9), (12, 10)}

# second run, resolving conficts
m = np.array([
    [ 0,  0, 0, 0, 0,  0, 0, 2, 0],
    [ 0,  0, 0, 3, 0,  0, 0, 2, 2],
    [ 0,  3, 0, 3, 0,  0, 2, 2, 2],
    [ 3,  3, 3, 3, 0,  7, 0, 0, 0],
    [ 3,  0, 0, 3, 3,  0, 0, 0, 0],
    [ 0,  0, 0, 0, 0,  0, 0, 0, 8],
    [ 0,  0, 0, 0, 0,  0, 8, 8, 8],
    [ 0, 10, 0, 0, 0,  8, 8, 8, 8],
    [10, 10, 0, 0, 0,  0, 0, 0, 8]
])

# fix value gaps
m = np.array([
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 2, 0, 0, 0, 1, 1],
    [0, 2, 0, 2, 0, 0, 1, 1, 1],
    [2, 2, 2, 2, 0, 3, 0, 0, 0],
    [2, 0, 0, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 4, 4, 4],
    [0, 5, 0, 0, 0, 4, 4, 4, 4],
    [5, 5, 0, 0, 0, 0, 0, 0, 4]
])

_, labels = cv.connectedComponents(matrix.astype(np.uint8), connectivity=4)
print(f'Same? {np.array_equal(labels, m)}')

plt.subplot(1, 2, 1)
plt.imshow(matrix, cmap='gray')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.title('Ocenjene regije')
plt.imshow(m, cmap='okabe_ito')
plt.suptitle('a')

plt.waitforbuttonpress()
plt.close()

# b
im = cv.imread('./src/regions.png', cv.IMREAD_GRAYSCALE)

_, im = cv.threshold(im, 127, 255, cv.THRESH_BINARY)

nregions, rim, stats, centroid = cv.connectedComponentsWithStats(im.astype(np.uint8), connectivity=4)

print(f'b.) Stevilo regij: {nregions}')

for i in range(nregions):
    plt.subplot(2, 2, i + 1)
    plt.imshow(rim == i, cmap='gray')
plt.suptitle('b')
plt.waitforbuttonpress()
plt.close()

plt.subplot(1, 2, 1)
plt.imshow(im, cmap='gray')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.imshow(rim, cmap='okabe_ito')
plt.title('Result')
plt.suptitle('b')

plt.waitforbuttonpress()
plt.close()

# c
fig, ax = plt.subplots()
ax.imshow(rim, cmap='okabe_ito')

ax.scatter(centroid[1:, 0], centroid[1:, 1], c='red')

for i, (x, y, w, h, _) in enumerate(stats[1:]):
    ax.add_patch(pat.Rectangle((x - 0.5, y - 0.5), w, h, fill=False, edgecolor='red'))

    cx, cy = centroid[i+1]
    ax.text(x - 0.5, y - 2, f'Centroid: {cx:.1f}, {cy:.1f}\nOcrtan X: {x}, Y: {y}, W: {w}, H: {h}', color='white',)

fig.suptitle('c')
plt.waitforbuttonpress()
plt.close()

# d
kernal = np.asarray([
    [1, 1, 1],
    [1, 1, 1],
    [0, 1, 0]
], dtype=np.uint8)

matrix = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 0]
], dtype=np.uint8)

dialatem = np.array([
    [0, 0, 0, 2, 0, 0, 0, 2, 1],
    [0, 2, 2, 1, 2, 0, 2, 1, 2],
    [2, 1, 2, 1, 2, 2, 1, 1, 2],
    [1, 1, 1, 1, 2, 1, 2, 2, 2],
    [1, 2, 2, 1, 1, 2, 2, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 0],
    [0, 2, 0, 0, 0, 2, 1, 1, 2],
    [2, 1, 2, 0, 2, 1, 1, 1, 2]
])

dialatem[dialatem > 1] = 1
# [[0 0 0 1 0 0 0 1 1]
#  [0 1 1 1 1 0 1 1 1]
#  [1 1 1 1 1 1 1 1 1]
#  [1 1 1 1 1 1 1 1 1]
#  [1 1 1 1 1 1 1 0 0]
#  [1 1 1 1 1 1 1 1 0]
#  [0 1 0 0 0 1 1 1 1]
#  [1 1 1 0 1 1 1 1 1

target = cv.dilate(matrix, kernal)
print(f'd.) Same, dialation? {np.array_equal(target, dialatem)}')

erosionm = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
])

target = cv.erode(matrix, kernal)
print(f'    Same, erosion?   {np.array_equal(target, erosionm)}')

# e
im = cv.imread('./src/regions_noise.png', cv.IMREAD_GRAYSCALE)

_, im = cv.threshold(im, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

nregions, rim, stats, _ = cv.connectedComponentsWithStats(im.astype(np.uint8))

print(f'e.) Regions areas: {stats[..., cv.CC_STAT_AREA]}')

# veliko regij zaradi artifaktov, regije so same po sebi majhne
plt.subplot(1, 2, 1)
plt.imshow(im, cmap='gray')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.imshow(rim, cmap='gray')
plt.title(f'Number of regions: {nregions}')
plt.suptitle('e')

plt.waitforbuttonpress()
plt.close()

# f
im = cv.imread('./src/regions_noise.png', cv.IMREAD_GRAYSCALE)

_, im = cv.threshold(im, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

rect = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
ellipsis = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10,10))
# rect = np.ones((5,5))

imre = cv.erode(im, rect)
imrd = cv.dilate(im, rect)

imee = cv.erode(im, ellipsis)
imed = cv.dilate(im, ellipsis)

plt.subplot(2, 2, 1)
plt.imshow(imre, cmap='gray')
plt.title('Erode rectangle kernal')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(imrd, cmap='gray')
plt.title('Dilate rectangle kernal')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(imee, cmap='gray')
plt.title('Erode elipse kernal')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(imed, cmap='gray')
plt.title('Dilate elipse kernal')
plt.xticks([])
plt.yticks([])

plt.suptitle('f')
plt.waitforbuttonpress()
plt.close()

# g
im = cv.imread('./src/regions_noise.png', cv.IMREAD_GRAYSCALE)

_, im = cv.threshold(im, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

rect = cv.getStructuringElement(cv.MORPH_RECT, (3,3))

openr = cv.erode(im, rect)
openr = cv.dilate(openr, rect)

closr = cv.dilate(im, rect)
closr = cv.erode(closr, rect)

openm = cv.morphologyEx(im, cv.MORPH_OPEN, rect)
closm = cv.morphologyEx(im, cv.MORPH_CLOSE, rect)

print(f'g.) Enakost, Odprtje: {np.array_equal(openr, openm)}, Zaprtje: {np.array_equal(closr, closm)}')

plt.subplot(3, 2, (1, 2))
plt.imshow(im, cmap='gray')
plt.title('Original')

plt.subplot(3, 2, 3)
plt.imshow(openr, cmap='gray')
plt.title('Opening rocno')

plt.subplot(3, 2, 4)
plt.imshow(closr, cmap='gray')
plt.title('Closing rocno')

plt.subplot(3, 2, 5)
plt.imshow(openm, cmap='gray')
plt.title('Opening morphex')

plt.subplot(3, 2, 6)
plt.imshow(closm, cmap='gray')
plt.title('Closing morphex')

plt.suptitle('g part1')
plt.waitforbuttonpress()
plt.close()

imc = cv.imread('./src/regions.png', cv.IMREAD_GRAYSCALE)

closopen = cv.morphologyEx(closm, cv.MORPH_OPEN, rect)

plt.subplot(1, 3, 1)
plt.imshow(im, cmap='gray')
plt.title('Original')

plt.subplot(1, 3, 2)
plt.imshow(closopen, cmap='gray')
plt.title('Closing and opening')

plt.subplot(1, 3, 3)
plt.imshow(imc, cmap='gray')
plt.title('Clean image')
plt.suptitle('g part2')

plt.waitforbuttonpress()
plt.close()

# h
im = cv.imread('./src/bird.jpg', cv.IMREAD_GRAYSCALE)
# cropping branch
im[400:, :450] = 0
im[260:354, 203:239] = 0
im[315:354, 203:260] = 0
im[389:406, 309:347] = 0
im[245:265, 213:232] = 0

_, tim = cv.threshold(im, 51, 255, cv.THRESH_BINARY)

plt.subplot(1, 2, 1)
plt.imshow(tim, cmap='gray')

el = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10,10))
tim = cv.morphologyEx(tim, cv.MORPH_CLOSE, el, iterations=2)

plt.suptitle('h')

plt.subplot(1, 2, 2)
plt.imshow(tim, cmap='gray')

fig, (ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(bottom=0.3)
img1 = ax1.imshow(im, cmap='gray', vmin=0, vmax=255)
img2 = ax2.imshow(im, cmap='gray', vmin=0, vmax=255)

s_thr = Slider(plt.axes([0.2, 0.19, 0.6, 0.03]), 'Threshold', 0, 255, valinit=51, valstep=1)
s_k = Slider(plt.axes([0.2, 0.12, 0.6, 0.03]), 'Close kernel', 1, 75, valinit=10, valstep=1)
s_it = Slider(plt.axes([0.2, 0.05, 0.6, 0.03]), 'Close iters', 1, 10, valinit=2, valstep=1)

def update(_):
    _, tim = cv.threshold(im, int(s_thr.val), 255, cv.THRESH_BINARY)
    k = int(s_k.val)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (k, k))
    closed = cv.morphologyEx(tim, cv.MORPH_CLOSE, kernel, iterations=int(s_it.val))
    img1.set_data(tim)
    img2.set_data(closed)
    fig.canvas.draw_idle()

for s in (s_thr, s_k, s_it):
    s.on_changed(update)
update(None)
plt.show()