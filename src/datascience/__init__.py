import os
import sys
import logging

# format of each logging message
logging_str = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

# logs destination path and log file
log_dir='logs'
log_filepath=os.path.join(log_dir,'logging.log')

# creates folder 'logs' if doesn't exists
os.makedirs(log_dir,exist_ok=True)

# main configuration logger
logging.basicConfig(
    level=logging.INFO, # min level of logging (INFO and higher)
    format=logging_str, # log message format

    handlers=(
        logging.FileHandler(log_filepath), # safe to logging.log file
        logging.StreamHandler(sys.stdout), # write in consol
    )
)

# logger creation of name 'datasciencelogger'
logger=logging.getLogger('datasciencelogger')