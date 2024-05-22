import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Memuat gambar
image = cv.imread("kucing.jpeg")

# Memeriksa apakah gambar berhasil dimuat
if image is None:
    print("Gambar tidak ditemukan.")
else:
    # Membuat subplot
    fig, ax = plt.subplots(1, 3, figsize=(16, 8))

    # Skala gambar menjadi 0.15 kali dari ukuran aslinya
    image_scaled = cv.resize(image, None, fx=0.15, fy=0.15, interpolation=cv.INTER_LINEAR)
    ax[0].imshow(cv.cvtColor(image_scaled, cv.COLOR_BGR2RGB))
    ax[0].set_title("Linear Interpolation Scale")

    # Skala gambar menjadi 2 kali dari ukuran aslinya
    image_scaled_2 = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
    ax[1].imshow(cv.cvtColor(image_scaled_2, cv.COLOR_BGR2RGB))
    ax[1].set_title("Cubic Interpolation Scale")

    # Skewed scale: merubah ukuran gambar ke 200x400
    image_scaled_3 = cv.resize(image, (200, 400), interpolation=cv.INTER_AREA)
    ax[2].imshow(cv.cvtColor(image_scaled_3, cv.COLOR_BGR2RGB))
    ax[2].set_title("Skewed Interpolation Scale")

    # Menampilkan plot
    plt.show()