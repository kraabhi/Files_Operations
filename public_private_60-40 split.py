import os
import shutil
import sklearn
from sklearn.model_selection import train_test_split

path_public='C:/Users/admin/Desktop/practice_problems/test_characters'
path_private='C:/Users/admin/Desktop/practice_problems/private'
print(path_private)
file_public =os.listdir('C:/Users/admin/Desktop/practice_problems/test_characters')
file_private = os.listdir('C:/Users/admin/Desktop/practice_problems/private')
for i in file_public:
    print(os.mkdir(os.path.join('C:/Users/admin/Desktop/practice_problems/private',i)))
    #print(os.path.join('C:/Users/admin/Desktop/practice_problems/private',i))

    public, private = train_test_split(os.listdir(os.path.join(path_public,i)),test_size=0.4)
    print(len(public))
    print(len(private))

    for item in private:
        shutil.move(os.path.join(path_public,i,item),os.path.join(path_private,i,item))

