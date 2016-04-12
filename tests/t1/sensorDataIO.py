import datetime

mainlist = []

def max(datalist):
   biggest = datalist[0]
   for item in datalist:
      if biggest < item:
          biggest = item
   return biggest

def min(datalist):
   biggest = datalist[0]
   for item in datalist:
      if biggest > item:
          biggest = item
   return biggest

data = open("visdata.csv")

headers = data.readline()
print(headers)
templist = []
for line in data:
    line = line.strip()
    datalist = line.split(',')

    #print(datalist)
    #templist.append(float(datalist[1]))
    mainlist.append(datalist)
    dat = datetime(datalist[0])

#print(templist)