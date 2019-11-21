import os
import sys
import pandas as pd

input_dir         = sys.argv[1]
output_file       = sys.argv[2]
sub_dir           = os.listdir(input_dir)
final_list        = []

for sub in sub_dir:
	sub_dir_path  = input_dir+"/"+sub
	images        = os.listdir(sub_dir_path)
	for img in images:
		final_list.append({'label': img,'category':sub})

output_df = pd.DataFrame(final_list)
output_df.to_csv(output_file, index=False)