import os

path = "adjudication/all"
entities = {}
relations = {}
for c in os.listdir(path):
    if c not in entities:
        entities[c] = {}
    if c not in relations:
        relations[c] = {}
    for f in os.listdir(path+"/"+c):
        f_open = open(path+"/"+c+"/"+f, "r")
        text = f_open.read()
        lines = text.split("\n")
        for l in lines:
            if l.startswith("T"):
                print (l)
                entity = l.split("\t")[1].split(" ")[1]
                print(entity)
