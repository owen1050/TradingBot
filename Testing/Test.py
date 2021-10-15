f = open("out3.txt", "r")
data = f.read()

data = data.replace("[java]", "")
data = data.split("_____")

newData = []
for d in data:
    newData.append(d.split("~~~"))

for i in newData:
    i[0] = i[0].replace('\n','')
    i[0] = i[0].strip()
    for j in i:
        j = j.strip()
