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

    comp = np.zeros(img1.shape)
    comp += img1 != img2
    comp *= 255
    misc.imsave("comp_color_onlydif.png", comp)

    img1_mean = np.mean(img1, axis=-1)
    img2_mean = np.mean(img2, axis=-1)
    comp = np.zeros(img1_mean.shape)
    comp += img1_mean != img2_mean
    comp *= 255
    misc.imsave("comp_grayscale_onlydif.png", comp)

    # img1_mean = np.mean(img1, axis=-1)
    # img2_mean = np.mean(img2, axis=-1)
    # comp = img2_mean - img1_mean
    # misc.imsave("comp_grayscale_2-1.png", comp)
    #
    # notsame = np.zeros(img1_mean.shape, dtype=np.uint8)
    # notsame = notsame + (img1_mean != img2_mean)
    # misc.imsave("comp_grayscale_notsame.png", notsame*255)
    #
    # comp2 = img1.copy()
    # comp2[:,:,0] *= notsame
    # comp2[:,:,1] *= notsame
    # comp2[:,:,2] *= notsame
    # misc.imsave("comp_grayscale_onlydif1.png", comp2)
    # comp2 = img2.copy()
    # comp2[:,:,0] *= notsame
    # comp2[:,:,1] *= notsame
    # comp2[:,:,2] *= notsame
    # misc.imsave("comp_grayscale_onlydif2.png", comp2)
    #
    # comp = img1_mean - img2_mean
    # misc.imsave("comp_grayscale_1-2.png", comp)
    # temp = misc.imread("comp_grayscale_1-2.png")
    # comp = np.array(temp > 128, dtype=np.uint8)*255
    # misc.imsave("comp_grayscale_1-2_threshold.png", comp)
    #
    # comp2 = img1.copy()
    # comp2[temp < 128] = 0
    # misc.imsave("comp_grayscale_sub1.png", comp2)


def IOU_color(img1, img2):
    """
    in this function I take the two images, which are assumed to
    be correctly aligned and of the same shape, and I return the
    intersection over union. I define IOU in this case to mean
    the intersection (the number of pixels that have the same value)
    divided by the union (the number of pixels in the image).
    As such, the values becomes a kind of percentage of the images
    that is similar. The IOU I calculate here is based off of the color
    images.
    """
    assert img1.shape == img2.shape
    comp = img1 - img2
    misc.imsave("comp_color_1-2.png", comp)
    temp = misc.imread("comp_color_1-2.png")
    temp = np.mean(temp, axis=-1)
    comp = np.array(temp > 128, dtype=np.uint8)
    union = comp.shape[0]*comp.shape[1]
    intersection = union - np.sum(comp)
    iou = intersection / float(union)

    comp *= 255
    misc.imsave("comp_color_1-2_threshold.png", comp)

    comp2 = img1.copy()
    comp2[temp < 128] = 0
    misc.imsave("comp_color_sub1.png", comp2)

    return iou


def IOU_grayscale(img1, img2):
    """
    in this function I take the two images, which are assumed to
    be correctly aligned and of the same shape, and I return the
    intersection over union. I define IOU in this case to mean
    the intersection (the number of pixels that have the same value)
    divided by the union (the number of pixels in the image).
    As such, the values becomes a kind of percentage of the images
    that is similar. The IOU I calculate here is based off of the grayscaled
    images.
    """
    assert img1.shape == img2.shape
    img1_mean = np.mean(img1, axis=-1)
    img2_mean = np.mean(img2, axis=-1)
    comp = img1_mean - img2_mean
    misc.imsave("comp_grayscale_1-2.png", comp)
    temp = misc.imread("comp_grayscale_1-2.png")
    comp = np.array(temp > 128, dtype=np.uint8)
    union = comp.shape[0]*comp.shape[1]
    intersection = union - np.sum(comp)
    iou = intersection / float(union)

    comp *= 255
    misc.imsave("comp_grayscale_1-2_threshold.png", comp)

    comp2 = img1.copy()
    comp2[temp < 128] = 0
    misc.imsave("comp_grayscale_sub1.png", comp2)

    return iou



def main():
    img1, img2 = read_images()

    compare_images(img1, img2)

    iou = IOU_color(img1, img2)
    print('iou of color images:', iou)
    iou = IOU_grayscale(img1, img2)
    print('iou of grayscale images:', iou)

if __name__ == '__main__':
    main()
