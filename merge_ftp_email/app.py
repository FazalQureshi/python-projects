# Imports
from merger import *
from notification import *
from ftp import *
from logger import *


# Download from ftp server

download_files()

# merge

z = merger()

# Upload to FTP

upload_file(z)