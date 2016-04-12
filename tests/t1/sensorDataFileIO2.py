import datetime

data = open("visdata.csv")

# Variables
datalist = []
mainlist = []
datelist = []

# Print the headers
headers = data.readline()
print(headers)

# Read the file and store all values
for line in data:
    line = line.strip()
    datalist = line.split(',')
    mainlist.append(datalist)
    datelist = datetime(datalist[0])
    print(datelist)