import numpy as np
import cv2
import matplotlib.pyplot as plt

# a.) 3 bitna slikovna slika 2^3
im3 = np.asarray(
[[5, 3, 2, 7, 1],
 [7, 1, 0, 0, 0],
 [4, 5, 7, 1, 1],
 [1, 3, 2, 1, 1],
 [5, 3, 1, 6, 3]]
)

def nrdi_hist(n, hist, x=8):
    plt.bar(np.arange(x), hist)
    plt.xticks(np.arange(x))
    plt.suptitle(n)
    plt.title(f'Histogram: {hist}')
    plt.waitforbuttonpress()
    plt.close()

tim = np.reshape(im3, -1)

# hist = np.bincount(tim) 
# hist = np.histogram(tim, bins=2, range=(0, 8))
#          [25, 1]    ==    [8, ] = [25, 8]
hist = (tim[:, None] == np.arange(8)).sum(axis=0)
nrdi_hist('a', hist)

# b.)
# kum_hist = np.cumsum(hist))
kum_hist = np.tri(8, dtype=int) @ hist
nrdi_hist('b', kum_hist)

# c.) odvisno koliko kosev bi imeli, glede na bite bi nas
# histogram lahko zavzemal vrednosti med 0 in 15 (2^4 = 16)
# kar pomeni da imamo lahko 16 binnov, 8, 4 ali celo 1
# zelo odvisno kaj zelimo da nas histogram prikazuje
im4 = np.random.randint(0, 16, (5, 5))
tim = np.reshape(im4, -1)
hist = np.bincount(tim, minlength=16)
nrdi_hist("c", hist, 16)

# d.)
im = cv2.imread('./src/umbrellas.jpg', cv2.IMREAD_GRAYSCALE)

# im = im.astype(np.float32)
# im = np.mean(im, axis=2)
hist, _ = np.histogram(im, bins=8)
x = np.arange(len(hist))

plt.subplot(1, 2, 1)
plt.imshow(im, cmap='gray')
plt.title('Sivinska slika')
plt.suptitle('d')
plt.subplot(1, 2, 2)
plt.bar(x, hist)
plt.title('Histogram sivinske slike')
plt.waitforbuttonpress()
plt.close()

hist, _ = np.histogram(im3, bins=16, range=(0, 15))
plt.bar(np.arange(16), hist)
plt.title('Histogram iz a.) 3bitna')
plt.suptitle('d')
plt.waitforbuttonpress()
plt.close()

# e.)
def histogram_stretch(im):
    a = 0 # min v 2^8
    b = 255 # max v 2^8
    c = np.min(im) # min v hist
    d = np.max(im) # max v hist

    # tim = (im - c) * ((b-a) / (d-c)) + a # net formula
    # tim = (im - c) * (255 / (d - c)) # lani formula
    tim = 255 * ((im - c) / (d - c)) # letos formula
    tim = (np.round(tim)).astype(np.uint8)

    return tim

im = cv2.imread('./src/phone.jpg')
tim = histogram_stretch(im.astype(np.float32))

im = (np.round(im)).astype(np.uint8)

hist = np.reshape(im, -1)
hist = np.bincount(hist, minlength=256)

thist = np.reshape(tim, -1)
thist = np.bincount(thist)

plt.subplot(2, 2, 1)
plt.imshow(im)
plt.title("Image")
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.stairs(hist)
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(tim)
plt.xticks([])
plt.yticks([])

plt.title("Fixed contrast")
plt.subplot(2, 2, 4)
plt.stairs(thist)
plt.yticks([])
plt.suptitle('e')

plt.waitforbuttonpress()
plt.close()

# f.) https://docs.opencv.org/3.4.20/d7/d4d/tutorial_py_thresholding.html
im = cv2.imread("./src/bird.jpg", cv2.IMREAD_GRAYSCALE)

# im = cv2.imread("./src/bottle/2026-10-19-202233.jpg", cv2.IMREAD_GRAYSCALE)
# hist, _ = np.histogram(im, bins=255)
# plt.subplot(1, 2, 1)
# plt.stairs(hist)
# plt.subplot(1, 2, 2)
# im = cv2.equalizeHist(im)
# hist, _ = np.histogram(im, bins=255)
# plt.stairs(hist)
# plt.show()

plt.subplot(2, 2, 1)
plt.imshow(im, cmap='gray')
plt.title("Original")

tim = im < 50
plt.subplot(2, 2, 2)
plt.imshow(tim, cmap='gray')
plt.title("Based on histogram")

plt.subplot(2, 2, 3)
_, tim = cv2.threshold(im, 50, 255, cv2.THRESH_BINARY)
plt.imshow(tim, cmap='gray')
plt.title("Based on histogram (thresh)")

plt.subplot(2, 2, 4)
_, tim = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(tim, cmap='gray')
plt.title("Otsu")
plt.suptitle('f')

plt.waitforbuttonpress()
plt.close()

# g.)
# Deluje najboljsse ko je histogram bimodalen (ima dva jasna vrha)
# in dolina vmes je ogromna, drugace povedano, ko imamo jasno razliko
# med ozadnjem in predmetom, ki ga zelimo izpostaviti
plt.stairs(hist)
plt.suptitle('g')
plt.title('Bimodalen histogram')
plt.show()


