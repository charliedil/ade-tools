"""
Step 1. Creates all folders per category.

Run instructions
----------------
INPUT: Path to dataset
OUTPUT: all folders per category

Example run:

python create_all_folders.py /home/user/ade/jenny

"""
import os
import os.path
from os import path
import shutil
import sys


abs = sys.argv[1]  # Get path
categories = ["consult", "discharge_summary", "general", "nursing", "pharmacy", "physician"]  # dataset categories
if not os.path.exists(abs + "/all/"):  # check to see if it exists first
    os.mkdir(abs + "/all")  # if not, create
for c in categories:
    if not os.path.exists(abs+"/all/"+c):  # same deal here
        os.mkdir(abs+"/all/"+c)

for folder in os.listdir(abs):  # Go through rounds
    if path.isdir(abs+"/"+folder) and folder!="all":
        for cat in os.listdir(abs+"/"+folder):  # Go through categories
            if path.isdir(abs + "/" + folder+"/"+cat):
                for file in os.listdir(abs + "/" + folder+"/"+cat):  # Copy over files
                    if file.endswith(".ann") or file.endswith(".txt"):
                        shutil.copy(abs+"/"+folder+"/"+cat+"/"+file, abs+"/all/"+cat)
