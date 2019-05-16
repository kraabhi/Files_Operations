import os
import shutil

for root, dirs, files in os.walk('C:/Users/admin/Desktop/practice_problems/test_characters'):  # replace the . with your starting directory
    for file in files:
        path_file = os.path.join(root,file)
        shutil.copy2(path_file,'C:/Users/admin/Desktop/practice_problems/test_characters_new') # change you destination dir
