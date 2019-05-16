import os, sys
import numpy as np
from scipy import misc
from scipy import ndimage


def read_points(file):
    with open(file, 'r') as f:
        lines = [[int(val) for val in line.strip().split()]
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
    for i in range(pt_dimp):
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
    pts, pts_prime = get_pts(bef[:3], aft[:3])
    ptsi = np.linalg.inv(pts)
    affine = np.dot(ptsi, pts_prime)

    chek = np.matmul(pts, affine)
    assert np.sum(np.rint(chek) == np.rint(pts_prime)) == chek.shape[0]

    pts2, pts_prime2 = get_pts(bef[3:6], aft[3:6])
    ptsi2 = np.linalg.inv(pts2)
    affine2 = np.dot(ptsi2, pts_prime2)
    chek2 = np.matmul(pts2, affine2)
    assert np.sum(np.rint(chek2) == np.rint(pts_prime2)) == chek2.shape[0]

    chek3 = np.matmul(pts, affine2)
    chek4 = np.matmul(pts2, affine)

    print(chek)
    print(chek2)
    print(chek3)
    print(chek4)
    assert np.sum(np.rint(chek3) == np.rint(pts_prime2)) == chek3.shape[0]

    assert np.sum(affine == affine2) == affine.shape[0]
    return a


def main():
    bef = "test_data/2D_registration/correspondence2D_w0.txt"
    aft = "test_data/2D_registration/correspondence2D_w1.txt"
    # bef = "taffine_test1.txt"
    # aft = "taffine_test2.txt"
    bef = read_points(bef)
    aft = read_points(aft)
    assert len(bef) == len(aft)
    pt_dim = len(bef[0])+1
    assert len(bef) >= pt_dim

    affine = get_affine(bef, aft)
    print( affine )

    # pts = np.zeros((len(bef)*2, pt_dim*2))
    # pts_prime = np.zeros((len(bef)*(pt_dim-1),))
    # for i in range(3):
    #     j = i*2
    #     k = j+1
    #     pts[j,0] = bef[i][0]
    #     pts[j,1] = bef[i][1]
    #     pts[j,2] = 1
    #     pts[k,3] = bef[i][0]
    #     pts[k,4] = bef[i][1]
    #     pts[k,5] = 1
    #
    #     pts_prime[j] = aft[i][0]
    #     pts_prime[k] = aft[i][1]
    #
    # print('shapes:',pts.shape, pts_prime.shape)
    # print('pts:',pts)
    # print('pts_prime:',pts_prime)
    # ptsi = np.linalg.inv(pts)
    # print('ptsi:',ptsi.shape)
    # a = np.dot(ptsi, pts_prime)
    # print('a.shape:',a.shape)
    # print('a:',a)
    #
    # b = np.matmul(pts, a)
    # print('b.shape:',b.shape)
    # print('b:',b)


if __name__ == '__main__':
    main()
