import os
import subprocess
import cv2
import numpy as np
count=170
name_mapping = {}
path = '/home/stark/cax/beer/Beer_Dataset/Test_data_complete/heb_test_data'
for dirs,subdir,files in os.walk('/home/stark/cax/beer/Beer_Dataset/Test_data_complete/heb_test_data'):
    for f in files:
        fff = os.path.join(dirs,f)
        img = cv2.imread(fff)
        count+=1
        print(fff)
        name = "cax"+str(count)
        fff = fff.split('/')[-1]
        name_mapping[fff] = name
        cv2.imwrite(str(name)+'.jpg',img)
        print(count)
        

np.save('my_file.npy', name_mapping)

