import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

#Required Folders and Files
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trails.ipynb"
    "requirements.txt",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) # To handle '/' as in windows we use '\'
    #seperate folders and files
    filedir , filename = os.path.split(filepath)
    if  filedir !="":
        # create folders if not exists
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Folder {filedir} created for the file {filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"File {filename} already exists.")