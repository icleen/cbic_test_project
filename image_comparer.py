import os, sys
import numpy as np
from scipy import misc
from scipy import ndimage

def read_images():
    img1_path = "test_data/diff_test/test_image_1.png"
    img2_path = "test_data/diff_test/test_image_2.png"
    img1 = misc.imread(img1_path)
    img2 = misc.imread(img2_path)
    return img1, img2

def compare_images(img1, img2):
    assert img1.shape == img2.shape
    comp = img1 - img2
    misc.imsave("comp_1-2.png", comp)
    comp = img2 - img1
    misc.imsave("comp_2-1.png", comp)

    comp = np.ones(img1.shape)
    comp = comp - (img1 == img2)
    misc.imsave("comp_onesbutdif.png", comp)

    img1_mean = np.mean(img1, axis=-1)
    img2_mean = np.mean(img2, axis=-1)
    comp = img2_mean - img1_mean
    misc.imsave("comp_grayscale_2-1.png", comp)

    notsame = np.zeros(img1_mean.shape, dtype=np.uint8)
    notsame = notsame + (img1_mean != img2_mean)
    misc.imsave("comp_grayscale_notsame.png", notsame*255)

    comp2 = img1.copy()
    comp2[:,:,0] *= notsame
    comp2[:,:,1] *= notsame
    comp2[:,:,2] *= notsame
    misc.imsave("comp_grayscale_onlydif1.png", comp2)
    comp2 = img2.copy()
    comp2[:,:,0] *= notsame
    comp2[:,:,1] *= notsame
    comp2[:,:,2] *= notsame
    misc.imsave("comp_grayscale_onlydif2.png", comp2)

    comp = img1_mean - img2_mean
    misc.imsave("comp_grayscale_1-2.png", comp)
    temp = misc.imread("comp_grayscale_1-2.png")
    comp = np.array(temp > 128, dtype=np.uint8)*255
    misc.imsave("comp_grayscale_1-2_threshold.png", comp)

    comp2 = img1.copy()
    comp2[temp < 128] = 0
    misc.imsave("comp_grayscale_sub1.png", comp2)


def main():
    img1, img2 = read_images()

    compare_images(img1, img2)

if __name__ == '__main__':
    main()
