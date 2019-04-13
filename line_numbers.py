filepath = 'text/iliad.txt'  
enumerated_txt = {}
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
       enumerated_txt[cnt] = line
    print(enumerated_txt[1])
