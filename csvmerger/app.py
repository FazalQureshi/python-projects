# Import
import os, glob
import pandas as pd
from pathlib import Path
os.chdir(Path(__file__).parent)

# Get all csv files in a folder
all_files = glob.glob(os.path.join("*.csv"))

#loop over datasets to make a list
all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f
    all_df.append(df)

# merge the list axis 0
merged_df = pd.concat(all_df, ignore_index=True, sort=False)

# move file name to the last column
file_name = merged_df.pop("file")
merged_df.insert(len(merged_df.columns), "file", file_name)

# save a the file
merged_df.to_csv('merged_df.csv',index=False,sep=',')
