"""
Attempt to fix multiline spanning entities. This code will do its best using the given spans to fix multiline entities.
Sometimes it cant, and for those that it cant, it will print the path.

BEWARE - this will write over the files you
provide, so ensure you have a backup.


Run instructions

INPUT
path to dataset

OUTPUT
paths to files that could not be fixed

Run with:
python multiline_entity_fixer.py path/to/dataset
"""



import os
import sys


path = sys.argv[1]
for r in os.listdir(path):
    if r!="all":
        for c in os.listdir(path+"/"+r):
            if not c.startswith("."):
                for file in os.listdir(path+"/"+r+"/"+c):
                    if file.endswith(".ann"):
                        f = open(path+"/"+r+"/"+c+"/"+file, "r")
                        lines = f.read().split("\n")
                        f.close()
                        outlines = []
                        for l in lines:
                            if "\t" not in l and l !="":
                                ## first check if the current span is correct
                                prev = outlines[len(outlines)-1]
                                try:
                                    length = int(prev.split("\t")[1].split(" ")[2])-int(prev.split("\t")[1].split(" ")[1])
                                    if len(prev.split("\t")[2]) + len(l) + 1 == length:
                                        outlines[len(outlines) - 1] += " " + l
                                    elif len(prev.split("\t")[2]) != length:
                                        print(path + "/" + r + "/" + c + "/" + file)
                                        outlines.append(l)
                                except(Exception):
                                    print("Exception in file: "+path + "/" + r + "/" + c + "/" + file)
                                    outlines.append(l)

                            else:
                                outlines.append(l)
                        f = open(path + "/" + r + "/" + c + "/" + file, "w")
                        for i in range(len(outlines)):
                            f.write(outlines[i])
                            if i!=len(outlines)-1:
                                f.write("\n")
                        f.close()


