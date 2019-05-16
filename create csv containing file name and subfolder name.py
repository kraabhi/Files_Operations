import os
import sys
import pandas as pd

input_dir         = "C:/Users/admin/Documents/Cax/Contest_characters/test"
output_file       = "C:/Users/admin/Documents/Cax/Contest_characters/actuals_character.csv"
sub_dir           = os.listdir(input_dir)
final_list        = []

for sub in sub_dir:
	sub_dir_path  = input_dir+"/"+sub
	images        = os.listdir(sub_dir_path)
	for img in images:
		final_list.append({'label': img,'category':sub})

output_df = pd.DataFrame(final_list)
output_df.to_csv(output_file, index=False)
