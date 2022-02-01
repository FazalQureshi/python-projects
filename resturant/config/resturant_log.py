
import logging
from logging.config import fileConfig
import os
from pathlib import Path
os.chdir(Path(__file__).parent)

fileConfig("logging.ini")
logger = logging.getLogger()

#logger.info("Application is started")