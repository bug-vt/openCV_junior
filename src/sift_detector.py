#!usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
import PIL import Image
import cv2


def linear_filter(img_in, kernel):
  '''Filter an input image by applying cross-correlation with a kernel.

  Input: 
    img_in: a grayscale image of any size larger than the kernel
    kernel: a 2D array of floating-point values;
     you may assume that this array is square, 
     with an odd number of rows and an odd number of columns;
     use the *center* of this kernel as its point of reference for filtering.

  Output:
    img_out: an image with the same row/column size as img_in, 
     but each pixel is a floating-point value;
     apply the kernel only at locations where it fits entirely within the 
     input image; 
     the remaining pixels (near the outside border of the output image)
     must be set to zero;
     for any negative values, take the absolute value;
     clip the final output so that every pixel value lies in the range 0 to 255.

  TO DO: implement the function.
  '''
  flipped_kernel = np.flip(np.flip(kernel, 0), 1)
  padding = kernel.shape[0] // 2
  img_copy = np.pad(np.copy(img_in), padding)
  img_out = np.zeros((img_copy.shape[0], img_copy.shape[1]), dtype=np.float32) 

  # perform cross-correlation between padded img and flipped kernel
  for row in range(padding, img_copy.shape[0] - padding):
    for col in range(padding, img_copy.shape[1] - padding):
      sample = img_copy[row-padding:row+padding+1, col-padding:col+padding+1]
      img_out[row][col] = np.sum(np.multiply(sample, flipped_kernel))

      # making pixel value range between 0 to 255
      if img_out[row][col] < 0:
        img_out[row][col] = abs(img_out[row][col])
      if img_out[row][col] > 255:
        img_out[row][col] = 255
      
  
  # remove the artifact from padding and return output img
  return img_out[padding:img_out.shape[0] - padding,
                 padding:img_out.shape[1] - padding] 
                 # Each pixel must be of type np.float32


def gaussian(x, y, sigma):
  return np.exp(-(x**2 + y**2) / (2 * sigma**2)) / (2 * np.pi * sigma**2)

def gaussianKernel(sigma, size = 9):
  mid = size // 2
  kernel = [[gaussian(col - mid, row - mid, sigma) for col in range(size)]
            for row in range(size)]
  return np.array(kernel, dtype=np.float32)


def sift_detector(img, nfeatures, threshold, sigma=1.6):
    s = 1.4
    levels = 5
    g_kernel = gaussianKernel(sigma)
    img_stack = [linear_filter(img, g_kernel*s**i) for i in range(levels)]
    



def main():
    



if __name__ == '__main__':
    main()
