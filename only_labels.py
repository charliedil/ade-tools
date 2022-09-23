"""
Checking data for anything outside the scope of the labels

Run Instructions

INPUT
Path to dataset to check

OUTPUT
Path to file with invalid entity label

EXAMPLE RUN
python only_labels.py path/to/dataset

path/to/dataset/round_1/consult/12345.ann
...
"""

labels = ["Drug","Dosage","Strength","Duration","Form","ADE", "Frequency","Reason","Route"]



import os
import sys

abs = sys.argv[1]

for r in os.listdir(abs):
    if r != "all":
        for c in os.listdir(abs+"/" + r):
            if not c.startswith(".") and not c.endswith(".conf")  and not c.endswith(".pl"):
                for f in os.listdir(abs+"/"+r+"/"+c):
                    if f.endswith(".ann"):
                        file = open(abs+"/"+r+"/"+c+"/"+f, "r")
                        text = file.read()
                        lines = text.split("\n")
                        for line in lines:
                            if line.startswith("T") and line!="":
                                try:
                                    if line.split("\t")[1].split(" ")[0] not in labels:
                                        print(abs+"/"+r+"/"+c+"/"+f)
                                        print(line.split("\t")[1].split(" ")[0])
                                except:
                                    print(abs+"/"+r+"/"+c+"/"+f)
                                    print(line)
