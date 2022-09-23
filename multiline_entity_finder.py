import os

for r in os.listdir("/home/charlie/ade/jessica/"):
    if r != "all" and not r.startswith("."):
        for c in os.listdir("/home/charlie/ade/jessica/" + r):
            if not c.startswith(".") and not c.endswith(".conf")  and not c.endswith(".pl"):
                for f in os.listdir("/home/charlie/ade/jessica/"+r+"/"+c):
                    if f.endswith(".ann"):
                        file = open("/home/charlie/ade/jessica/"+r+"/"+c+"/"+f, "r")
                        text = file.read()
                        lines = text.split("\n")
                        for line in lines:
                            if "\t" not in line and line!="":
                                print("/home/charlie/ade/jessica/"+r+"/"+c+"/"+f)
                                print(line)
