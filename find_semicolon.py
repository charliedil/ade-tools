import os

for r in os.listdir("/home/charlie/ade/adjudication"):
    if r != "all":
        for c in os.listdir("/home/charlie/ade/adjudication/" + r):
            if not c.startswith(".") and not c.endswith(".conf")  and not c.endswith(".pl") and c!="all":
                for f in os.listdir("/home/charlie/ade/adjudication/"+r+"/"+c):
                    if f.endswith(".ann"):
                        file = open("/home/charlie/ade/adjudication/"+r+"/"+c+"/"+f, "r")
                        text = file.read()
                        lines = text.split("\n")
                        file.close()
                        for line in lines:
                            if ";" in line:
                                if line.split("\t")[1].split(" ")[1].startswith(";"):
                                    print("/home/charlie/ade/adjudication/" + r + "/" + c + "/" + f)
                                    print(line)
                                else:
                                    file = open("/home/charlie/ade/adjudication/"+r+"/"+c+"/"+f, "w")
                                    for line in lines:
                                        if ";" not in line or line.split("\t")[1].split(" ")[1].startswith(";"):
                                            file.write(line)
                                            file.write("\n")
                                        else:
                                            file.write(line.split("\t")[0]+"\t")
                                            file.write(line.split("\t")[1].split(" ")[0]+ " ")
                                            file.write(line.split("\t")[1].split(" ")[1]+ " ")
                                            file.write(line.split("\t")[1].split(" ")[len(line.split("\t")[1].split(" "))-1] + "\t")
                                            file.write(line.split("\t")[2]+"\n")

