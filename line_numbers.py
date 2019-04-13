# import json

filepath = 'text/simple.txt'  
enumerated_txt = {}
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        enumerated_txt[cnt] = line.rstrip()
        # num,words = cnt+1,line.split()
        # print(line.rstrip())

print(enumerated_txt)
# fileout = "dict.json"
# json = json.dumps(enumerated_txt)
# f = open(fileout,"w")
# f.write(json)
# f.close()