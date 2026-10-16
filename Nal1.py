import cv2
import matplotlib.pyplot as plt
import numpy as np

ime_slike = './src/umbrellas.jpg'
im = cv2.imread(ime_slike)
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)


print(f'Oblika: {im.shape=}')
print(f'Data type: {im.dtype=}')

tim = im.astype(np.float32)
tim = np.mean(tim, axis=2)

for i, val in enumerate((None, 'gray', 'jet', 'bone')):
    plt.subplot(1, 4, i+1)
    plt.imshow(tim, cmap=val)
    plt.title(val)

plt.waitforbuttonpress()
plt.close()

tim = im[100:250, 200:400, ...].copy()
tim[..., 2] = 0

plt.subplot(1, 2, 1)
plt.imshow(tim)
plt.subplot(1, 2, 2)
plt.imshow(im)
plt.show()