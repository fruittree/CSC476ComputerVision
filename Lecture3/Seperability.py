import numpy as np
import cv2
from scipy import ndimage

im = np.array([[2,3,3],[3,5,5],[4,4,6]])

mkernal = np.array([[1,2,1],[2,4,2],[1,2,1]])

mkernal_row = np.array([1,2,1])

out = np.outer(np.transpose(mkernal_row),mkernal_row)

res = ndimage.convolve(im,mkernal,mode="constant")

res1 = ndimage.filters.convolve1d(im,mkernal_row,mode="constant",axis=0)
res2 = ndimage.filters.convolve1d(res1,np.transpose(mkernal_row),mode="constant", axis=1)



