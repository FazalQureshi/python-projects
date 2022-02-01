# Import
from notification import *
from logger import *
import os, glob
import pandas as pd
from pathlib import Path
os.chdir(Path(__file__).parent)

def merger():
    logger.info("Merge will start") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~logger
    try:
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

        logger.info("Merge is saved as csv file") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~logger
        # save a the file
        name_of_file = input('Enter the name of merged file: ')
        merged_df.to_csv(f'{name_of_file}.csv',index=False,sep=',')

        return name_of_file

    except:
        notify("Merge failed", "Merge Notification") 
