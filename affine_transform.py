import os, sys
import numpy as np
from scipy import misc
from scipy import ndimage
from PIL import Image
import matplotlib.pyplot as plt


def read_points(file):
    with open(file, 'r') as f:
        lines = [[float(val) for val in line.strip().split()]
                                for line in f if len(line) > 1]
    # print(file)
    # for line in lines:
    #     print(line)
    return lines


def get_pts(bef, aft):
    pt_dim = len(bef[0])
    pt_dimp = pt_dim+1
    pts = np.zeros((len(bef)*pt_dim, pt_dimp*2))
    pts_prime = np.zeros((len(bef)*pt_dim,))
    for i in range(len(bef)):
        j = i*pt_dim
        for ind in range(pt_dim):
            pts[j,ind] = bef[i][ind]
            pts[j+1,ind+pt_dimp] = bef[i][ind]
        pts[j,pt_dim] = 1
        pts[j+1,pt_dim+pt_dimp] = 1

        for ind in range(pt_dim):
            pts_prime[j+ind] = aft[i][ind]
    return pts, pts_prime


def get_affine(bef, aft):
    pts, pts_prime = get_pts(bef, aft)
    ptsi = np.linalg.pinv(pts)
    affine = np.dot(ptsi, pts_prime)

    # import pdb; pdb.set_trace()
    # chek = np.matmul(pts, affine)
    # assert np.sum(np.rint(chek) == np.rint(pts_prime)) == chek.shape[0]
    #
    # pts2, pts_prime2 = get_pts(bef[3:6], aft[3:6])
    # ptsi2 = np.linalg.inv(pts2)
    # affine2 = np.dot(ptsi2, pts_prime2)
    # chek2 = np.matmul(pts2, affine2)
    # assert np.sum(np.rint(chek2) == np.rint(pts_prime2)) == chek2.shape[0]
    #
    # chek3 = np.matmul(pts, affine2)
    # chek4 = np.matmul(pts2, affine)
    #
    # print(chek)
    # print(chek2)
    # print(chek3)
    # print(chek4)
    # assert np.sum(np.rint(chek3) == np.rint(pts_prime2)) == chek3.shape[0]
    #
    # assert np.sum(affine == affine2) == affine.shape[0]

    return affine


def combine_imgs(img1, img2, affine):
    img1 = Image.open(img1)
    img2 = Image.open(img2)

    nwidth = img1.size[0] + img2.size[0]
    nheight = img1.size[1] + img2.size[1]

    imgt2 = img2.transform((nwidth, nheight),
        Image.AFFINE, data=affine.flatten()[:6], resample=Image.NEAREST)
    imgt2 = np.asarray(imgt2)

    result = np.zeros((nheight, nwidth))
    result += imgt2
    result[:img1.size[1], :img1.size[0]] = 0

    imgt1 = np.asarray(img1)
    shp = ((0, nheight-imgt1.shape[0]), (0, nwidth-imgt1.shape[1]))
    imgt1 = np.pad(imgt1, shp,
        'constant', constant_values=0)
    result += imgt1

    i, j = result.shape[0]-1, result.shape[1]-1
    while result[i,0] < 1:
        i -= 1
    while result[0,j] < 1:
        j -= 1

    result = result[:i, :j]
    plt.imsave('combined.png', result)
    # plt.imshow(result)
    # plt.show()


def main():
    bef = "test_data/2D_registration/correspondence2D_w0.txt" \
        if len(sys.argv) < 2 else sys.argv[1]
    aft = "test_data/2D_registration/correspondence2D_w1.txt" \
        if len(sys.argv) < 3 else sys.argv[2]
    # bef = "test_data/3D_registration/correspondence3D_0.txt"
    # aft = "test_data/3D_registration/correspondence3D_1.txt"
    bef = read_points(bef)
    aft = read_points(aft)
    assert len(bef) == len(aft)
    pt_dim = len(bef[0])+1
    assert len(bef) >= pt_dim

    affine = get_affine(bef, aft)
    print('affine:', affine)

    if len(sys.argv) < 2:
        img1 = 'test_data/2D_registration/w0.png'
        img2 = 'test_data/2D_registration/w1.png'
        combine_imgs(img1, img2, affine)


if __name__ == '__main__':
    main()
