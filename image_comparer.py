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


def IOU_color(img1, img2):
    """
    In this function I take the two images, which are assumed to
    be correctly aligned and of the same shape, and I return the
    intersection over union. I define IOU in this case to mean
    the intersection (the number of pixels that have the same value)
    divided by the union (the number of pixels in the image).
    As such, the values becomes a kind of percentage of the images
    that is similar. The IOU I calculate here is based off of the color
    images. As such, I simply sum up the number of pixels that are exactly
    the same between both images for the intersection.
    See below for an alternative process.
    """
    assert img1.shape == img2.shape

    notsame = img1 != img2
    notsame = np.max(notsame, axis=-1)
    comp = np.zeros(notsame.shape)
    comp += notsame
    comp *= 255
    misc.imsave("comp_color_onlydif.png", comp)

    union = notsame.shape[0]*notsame.shape[1]
    intersection = union - np.sum(notsame)
    iou = intersection / float(union)

    same = img1 == img2
    same = np.min(same, axis=-1)
    comp2 = img1.copy()
    comp2[same] = 0
    misc.imsave("comp_color_sub1.png", comp2)

    return iou


def IOU_grayscale(img1, img2):
    """
    In this function I take the two images, which are assumed to
    be correctly aligned and of the same shape, and I return the
    intersection over union. I define IOU in this case to mean
    the intersection (the number of pixels that have the same value)
    divided by the union (the number of pixels in the image).
    As such, the values becomes a kind of percentage of the images
    that is similar. The IOU I calculate here is based off of the grayscaled
    images. In particular, instead of simply calculating which pixels have
    the same grayscale value and which don't, I instead subtract one image
    the other and normalize, giving me an image where similar atributes
    have been subtracted out. I then threshold the resulting image, making
    each value a one or zero, and sum the result, which gives me the value
    for intersection. This is more rubust than simply calculating the
    intersection by summing the number of pixels that are exactly the same
    between images. Below I save out images that show the intermediary steps,
    visualizing the process step by step.
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

    iou = IOU_color(img1, img2)
    print('iou of color images:', iou)
    iou = IOU_grayscale(img1, img2)
    print('iou of grayscale images:', iou)

if __name__ == '__main__':
    main()
