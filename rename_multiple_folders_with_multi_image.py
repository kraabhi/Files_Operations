import os

os.chdir("C:\\Users\\admin\\Desktop\\practice_problems\\test_characters")

os.getcwd()
import os
import subprocess
import cv2
import numpy as np


path_test = "C:/Users/admin/Desktop/practice_problems/test_characters"
file_test = os.listdir(path_test)
print(file_test)
# loop over the files and split the names from the extension
j =0
for i in file_test:
#     print(os.path.join(path_test,i))
    os.chdir(os.path.join(path_test,i))
    for file in os.listdir(os.curdir):
        #print (os.path.splitext(file))
        file_name, file_extension = os.path.splitext(file)
        print(file_name)
        j += 1       
        new_file_name = 'Cax_test{}.jpg'.format(j)
        print(new_file_name)
        os.rename(file, new_file_name)
 
