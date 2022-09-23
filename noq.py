"""
Checking data for q_

Run Instructions

INPUT
Path to dataset you're checking

OUTPUT
Paths to files with q_'s

EXAMPLE RUN

python noq.py path/to/dataset

path/to/dataset/round_1/consult/12345.ann

"""

import os
from os import path
import sys
abs = sys.argv[1]
for r in os.listdir(abs):
    if r != "all" :
        for c in os.listdir(abs+"/" + r):
            if not c.startswith(".") and not c.endswith(".conf")  and not c.endswith(".pl"):
                for f in os.listdir(abs+"/"+r+"/"+c):
                    if f.endswith(".ann"):
                        file = open(abs+"/"+r+"/"+c+"/"+f, "r")
                        text = file.read()
                        if "q_" in text:
                            print(abs+"/"+r+"/"+c+"/"+f)

