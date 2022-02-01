from pandas.core.base import DataError
from merger import *
from notification import *
from datetime import datetime, time
from ftplib import FTP
from logger import *
import os
from pathlib import Path
os.chdir(Path(__file__).parent)

def login():
    server = "ngcobalt414.manitu.net"
    user_name = "ftp200015751"
    password = "A12345678@"

    ftp = FTP(server)
    ftp.login(user_name,password)
    

    ftp.cwd("Fazal")
    
    return ftp

def upload_file(c):

    up = login() 
    
    files = up.nlst()

    for file in files:
        if file == (c + ".csv"):
            print("File name already exists in the directory. It will be overwritten")
    
    file_to_upload = c + ".csv"

    up.storbinary("STOR " + file_to_upload, open(file_to_upload, mode = "rb"))

    up.quit()

    logger.info("Files uploaded") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~logger

    t = datetime.now()
    tstr = t.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    y = "Merge Upload Notification"
    x = "The Merge is uploaded Succesfully"

    notify(x, y)

def download_files():
    
    down = login()

    files = down.nlst()
    print(files)

    for file in files:
        print(file)

        root, ext = os.path.splitext(file)
        if ext:
            print("Downloading:...", file)
            
            local_file = open(root + "_downloaded" + ext, mode = "wb")

            down.retrbinary("RETR " + file, local_file.write)

            local_file.close()

    logger.info("Files downloaded") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~logger

    down.quit()


"""
#upload_file()

download_files()

# close the connection
ftp.quit()

print("Succesfully closed")
"""