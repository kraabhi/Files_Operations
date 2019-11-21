import os
import shutil
import sklearn
from sklearn.model_selection import train_test_split

path_train='/media/atul/CrowdANALYTIX/Lifung_PT_model/Datasets/Third/Train_lifung_third/Suspenders/'
path_test='/media/atul/CrowdANALYTIX/Lifung_PT_model/Datasets/Third/Test_lifung_third/Suspenders/'

file_train = os.listdir(path_train)
file_test = os.listdir(path_test)

train_superhero, test_superhero = train_test_split(file_train, test_size=0.2)
print(len(train_superhero))
print(len(test_superhero))

for item in test_superhero:
	shutil.move(path_train+'/'+item,path_test+'/'+item)
