import numpy as np
import cv2

from ps1 import *


def main():

    # Insert you image file names here
    img1_filename = None
    img2_filename = None

    # # 1a
    img1 = cv2.imread(img1_filename)
    img2 = cv2.imread(img2_filename)

    assert 100 < img1.shape[0] <= 512, "Check your image 1 dimensions"
    assert 100 < img1.shape[1] <= 512, "Check your image 1 dimensions"
    assert 100 < img2.shape[0] <= 512, "Check your image 2 dimensions"
    assert 100 < img2.shape[1] <= 512, "Check your image 2 dimensions"

    # # 2 Color Planes

    # # 2a
    swapped_red_blue_img = swapRedBlue(img1)
    cv2.imwrite('output/ps1-2-a-1.png', swapped_red_blue_img)

    # # 2b
    img1_green = extractGreen(img1)
    cv2.imwrite('output/ps1-2-b-1.png', img1_green)
    
    # # 2c
    img1_red = extractRed(img1)
    cv2.imwrite('output/ps1-2-c-1.png', img1_red)

    # # 3 Replacement of Pixels

    # # 3a
    mono1 = cv2.imread('output/ps1-2-b-1.png', cv2.IMREAD_GRAYSCALE)
    mono2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    replaced_img = copyPasteMiddle(mono1, mono2, (100, 100))
          
    cv2.imwrite('output/ps1-3-a-1.png', replaced_img)

    # # 4 Arithmetic and Geometric operations

    # # 4a
    min_green, max_green, mean_green, stddev_green = imageStats(img1_green)

    print("The min pixel value of img1_green is", min_green)
    print("The max pixel value of img1_green is", max_green)
    print("The mean pixel value of img1_green is", mean_green)
    print("The std dev of img1_green is", stddev_green)

    # # 4b
    img1_green = img1_green.astype('float64')
    normalized_img = normalized(img1_green, 10)
    cv2.imwrite('output/ps1-4-b-1.png', np.clip(normalized_img, 0, 255))

    # # 4c
    shift_green = shiftImageLeft(img1_green, 2)
    cv2.imwrite('output/ps1-4-c-1.png', shift_green)

    # # 4d
    diff_green = differenceImage(img1_green, shift_green)
    cv2.normalize(diff_green, diff_green, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite('output/ps1-4-d-1.png', diff_green)

    # # 5 Noise
    img1_f64 = img1.astype('float64')

    # Choose a sigma value
    sigma = None

    # # 5a
    channel = None
    noisy_green = addNoise(img1_f64, channel, sigma)
    cv2.imwrite('output/ps1-5-a-1.png', np.clip(noisy_green, 0, 255))

    # # 5b
    channel = None
    noisy_blue = addNoise(img1_f64, channel, sigma)
    cv2.imwrite('output/ps1-5-b-1.png', np.clip(noisy_blue, 0, 255))

if __name__ == "__main__":
    main()
