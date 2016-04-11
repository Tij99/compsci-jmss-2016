

data = open("visdata.csv")

headers = data.readline()
print(headers)

templist=[]
timelist=[]
lines = len(data.readline())
for line in data:
    line = line.strip()
    datalist = line.split(',')

    timelist.append(datalist[0])
    templist.append(float(datalist[1]))



print(templist)