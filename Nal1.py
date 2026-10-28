import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

ime_slike = './src/umbrellas.jpg'
im = cv2.imread(ime_slike)
assert im is not None
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

print(f'a.) Oblika: {im.shape=}')
print(f'Data type: {im.dtype=}')

# pretvorba in povprecenje po color channel, R + G + B / 3, rez sivinska
# b.)
tgim = im.astype(np.float32)
# tgim = (tgim[..., 0] + tgim[..., 1] + tgim[..., 2]) / 3
# tgim = tgim.sum(axis=2) / 3
tgim = np.mean(tgim, axis=2)

fig1 = plt.figure()
fig1.suptitle('a in b')
for i, val in enumerate((None, 'gray', 'jet', 'bone')):
    plt.subplot(2, 2, i+1)
    plt.imshow(tgim, cmap=val)
    plt.title(val)

plt.waitforbuttonpress()
plt.close()

# izrez in spreminjanje lokacije v originalu
# c.)
tim = im[100:250, 200:400, ...].copy()
im[100:250, 200:400, 2] = 0

fig2 = plt.figure()
fig2.suptitle('c')
plt.subplot(1, 2, 1)
plt.imshow(tim)
plt.subplot(1, 2, 2)
plt.imshow(im)
plt.waitforbuttonpress()
plt.close()

fig2 = plt.figure()
fig2.suptitle('d')

# 50 / 50 inverz, 255 ker vrednosti RGB 0 - 255
# d.)
tim = tgim.copy()
tim[:, :tim.shape[1]//2] = 255 - tgim[:, :tgim.shape[1]//2]

plt.imshow(tim, cmap='gray')
plt.waitforbuttonpress()
plt.close()

# fig3 = plt.figure()
# fig3.suptitle('e')
# uporaba maske za bool matrix
# e.)
# binim = tgim > 150
# plt.subplot(1, 2, 1)
# plt.imshow(tgim, cmap='gray')
# plt.title('Sivinska slika')
# plt.subplot(1, 2, 2)
# plt.imshow(binim, cmap='gray')
# plt.title('Binarna slika')

thr0 = 150

fig3 = plt.figure()
fig3.suptitle('e')
plt.subplots_adjust(bottom=0.2)

plt.subplot(1, 2, 1)
plt.imshow(tgim, cmap='gray', vmin=0, vmax=255)
plt.title('Sivinska slika')

ax_bin = plt.subplot(1, 2, 2)
shown = ax_bin.imshow(tgim > thr0, cmap='gray', vmin=0, vmax=1)
ax_bin.set_title(f'Binarna slika, prag {thr0}')

ax_slider = plt.axes([0.25, 0.05, 0.5, 0.04])
slider = Slider(ax_slider, 'Prag', 0, 255, valinit=thr0, valstep=1)

def update(val):
    thr = slider.val
    shown.set_data(tgim > thr)
    ax_bin.set_title(f'Binarna slika, prag {int(thr)}')
    fig3.canvas.draw_idle()

slider.on_changed(update)
plt.show()