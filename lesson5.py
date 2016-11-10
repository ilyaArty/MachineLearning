from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
im_arr = misc.imread('boy.png')
vert=im_arr.shape[0]
hor=im_arr.shape[1]
im_arr2 = np.zeros((vert,hor))
i=0
j=0

while i<vert:
    while j<hor:
        im_arr2[i,j]=im_arr[i,j,0]*0.299+im_arr[i,j,1]*0.587+im_arr[i,j,2]*0.144;
        j=j+1;
    j=0;
    i=i+1;
print(im_arr2)
plt.imshow(im_arr2, cmap='gray')
