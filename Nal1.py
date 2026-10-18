import cv2
import matplotlib.pyplot as plt
import numpy as np

ime_slike = './src/umbrellas.jpg'
im = cv2.imread(ime_slike)
assert im is not None
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

print(f'Oblika: {im.shape=}')
print(f'Data type: {im.dtype=}')
print(np.finfo(np.float32).max)

tgim = im.astype(np.float32)
tgim = np.mean(tgim, axis=2)

fig1 = plt.figure()
fig1.suptitle('a in b')
for i, val in enumerate((None, 'gray', 'jet', 'bone')):
    plt.subplot(2, 2, i+1)
    plt.imshow(tgim, cmap=val)
    plt.title(val)

plt.waitforbuttonpress()
plt.close()

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
tim = tgim.copy()
tim[:, :tim.shape[1]//2] = 255 - tgim[:, :tgim.shape[1]//2]
plt.imshow(tim, cmap='gray')
plt.waitforbuttonpress()
plt.close()

plt.show()